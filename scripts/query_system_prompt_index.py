#!/usr/bin/env python3
"""Query public System Prompt Index audit records without vendoring the corpus."""

from __future__ import annotations

import argparse
import datetime as dt
import json
import os
from pathlib import Path
import subprocess
import sys
from typing import Any, Iterable


REPO_URL = "https://github.com/SystemPromptIndex/SystemPromptIndex.git"
WEB_ROOT = "https://github.com/SystemPromptIndex/SystemPromptIndex/blob/main"
DIMENSIONS = {f"D{i}" for i in range(1, 9)} | {"Misc"}


class QueryError(RuntimeError):
    pass


def run_git(args: list[str], cwd: Path | None = None) -> str:
    result = subprocess.run(
        ["git", *args],
        cwd=cwd,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )
    if result.returncode:
        detail = result.stderr.strip() or result.stdout.strip() or "git command failed"
        raise QueryError(detail)
    return result.stdout.strip()


def resolve_dataset(repo: str | None, cache_dir: str | None, refresh: bool) -> Path:
    if repo:
        root = Path(repo).expanduser().resolve()
        if not root.is_dir():
            raise QueryError(f"dataset path does not exist: {root}")
    else:
        configured = cache_dir or os.environ.get("AI_PRODUCT_TEARDOWN_CACHE")
        root = Path(configured).expanduser() if configured else (
            Path.home() / ".cache" / "ai-product-teardown" / "system-prompt-index"
        )
        root = root.resolve()
        if not root.exists():
            root.parent.mkdir(parents=True, exist_ok=True)
            run_git(["clone", "--depth", "1", REPO_URL, str(root)])
        elif refresh:
            run_git(["pull", "--ff-only"], cwd=root)

    if not (root / "audits").is_dir() or not (root / "dimensions.json").is_file():
        raise QueryError(f"not a System Prompt Index dataset: {root}")
    return root


def dataset_commit(root: Path) -> str | None:
    try:
        return run_git(["rev-parse", "HEAD"], cwd=root)
    except QueryError:
        return None


def load_audits(root: Path) -> Iterable[tuple[Path, dict[str, Any]]]:
    for path in sorted((root / "audits").glob("*/*.json")):
        try:
            value = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as exc:
            print(f"warning: skipped {path}: {exc}", file=sys.stderr)
            continue
        if isinstance(value, dict):
            yield path, value


def match_score(query: str, path: Path, audit: dict[str, Any]) -> int:
    needle = query.casefold().strip()
    values = [
        str(audit.get("company", "")),
        str(audit.get("product", "")),
        str(audit.get("id", "")),
        path.stem,
    ]
    folded = [value.casefold() for value in values]
    if any(value == needle for value in folded):
        return 100
    if any(value.startswith(needle) for value in folded):
        return 70
    if any(needle in value for value in folded):
        return 40
    tokens = [token for token in needle.replace("-", " ").replace("_", " ").split() if token]
    return 10 if tokens and all(any(token in value for value in folded) for token in tokens) else 0


def prompt_path_for(root: Path, audit_path: Path) -> Path:
    relative = audit_path.relative_to(root / "audits").with_suffix(".md")
    return root / "prompts" / relative


def select_spans(
    audit: dict[str, Any],
    dimensions: set[str],
    span_type: str,
    max_spans: int,
    max_chars: int,
) -> list[dict[str, Any]]:
    def clip(value: Any) -> tuple[str, bool]:
        text = str(value or "")
        if len(text) <= max_chars:
            return text, False
        return text[: max_chars - 1].rstrip() + "…", True

    selected: list[dict[str, Any]] = []
    for raw in audit.get("spans", []):
        if not isinstance(raw, dict):
            continue
        dimension = str(raw.get("dimension", "Misc"))
        score = raw.get("score")
        risky = bool(raw.get("risky", False))
        if dimensions and dimension not in dimensions:
            continue
        if span_type == "protective" and score != 1:
            continue
        if span_type == "problematic" and score != -1:
            continue
        if span_type == "risky" and not risky:
            continue
        text, text_truncated = clip(raw.get("text"))
        note, note_truncated = clip(raw.get("note"))
        selected.append(
            {
                "text": text,
                "dimension": dimension,
                "score": score,
                "risky": risky,
                "note": note,
                "start": raw.get("start"),
                "end": raw.get("end"),
                "truncated": text_truncated or note_truncated,
            }
        )
        if len(selected) >= max_spans:
            break
    return selected


def build_record(
    root: Path,
    audit_path: Path,
    audit: dict[str, Any],
    dimensions: set[str],
    span_type: str,
    max_spans: int,
    max_chars: int,
) -> dict[str, Any]:
    audit_rel = audit_path.relative_to(root).as_posix()
    prompt_path = prompt_path_for(root, audit_path)
    prompt_rel = prompt_path.relative_to(root).as_posix()
    spans = select_spans(audit, dimensions, span_type, max_spans, max_chars)
    risky_count = sum(bool(span.get("risky")) for span in audit.get("spans", []) if isinstance(span, dict))
    return {
        "id": audit.get("id"),
        "company": audit.get("company"),
        "product": audit.get("product"),
        "category": audit.get("category"),
        "annotation": audit.get("annotation"),
        "protective_entries": audit.get("protective_entries", 0),
        "problematic_entries": audit.get("problematic_entries", 0),
        "risky_entries": risky_count,
        "by_dimension": audit.get("by_dimension", {}),
        "spans": spans,
        "audit_url": f"{WEB_ROOT}/{audit_rel}",
        "prompt_url": f"{WEB_ROOT}/{prompt_rel}" if prompt_path.is_file() else None,
        "authenticity": "unverified unless independently corroborated",
    }


def as_markdown(payload: dict[str, Any]) -> str:
    lines = [
        f"# System Prompt Index query: {payload['query']}",
        "",
        f"- Dataset commit: `{payload.get('dataset_commit') or 'unknown'}`",
        f"- Retrieved at: {payload['retrieved_at']}",
        f"- Matches: {len(payload['results'])}",
        "- Caveat: inclusion does not prove authenticity, currency, or production use.",
    ]
    for record in payload["results"]:
        lines.extend(
            [
                "",
                f"## {record.get('company')} — {record.get('product')}",
                "",
                f"- Annotation: `{record.get('annotation')}`",
                f"- Protective / problematic / risky: {record.get('protective_entries')} / {record.get('problematic_entries')} / {record.get('risky_entries')}",
                f"- [Audit source]({record.get('audit_url')})",
            ]
        )
        if record.get("prompt_url"):
            lines.append(f"- [Published prompt record]({record['prompt_url']})")
        for span in record["spans"]:
            label = "risky" if span["risky"] else ("protective" if span["score"] == 1 else "problematic")
            lines.extend(
                [
                    "",
                    f"> {span['text']}",
                    "",
                    f"`{span['dimension']}` · `{label}` · {span['note']}",
                ]
            )
    return "\n".join(lines) + "\n"


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Search public System Prompt Index audits with provenance and bounded spans."
    )
    parser.add_argument("query", help="Product, organization, or record identifier")
    parser.add_argument("--repo", help="Existing local SystemPromptIndex checkout")
    parser.add_argument("--cache-dir", help="Dataset cache directory used when --repo is omitted")
    parser.add_argument("--refresh", action="store_true", help="Fast-forward an existing cache before querying")
    parser.add_argument("--dimension", action="append", choices=sorted(DIMENSIONS), default=[])
    parser.add_argument(
        "--span-type", choices=("all", "protective", "problematic", "risky"), default="all"
    )
    parser.add_argument("--limit", type=int, default=5, help="Maximum matching prompt records")
    parser.add_argument("--max-spans", type=int, default=8, help="Maximum spans per prompt record")
    parser.add_argument(
        "--max-chars", type=int, default=600, help="Maximum characters per span text or note"
    )
    parser.add_argument("--format", choices=("json", "markdown"), default="json")
    args = parser.parse_args(argv)
    if args.limit < 1 or args.max_spans < 0 or args.max_chars < 40:
        parser.error("--limit must be positive, --max-spans non-negative, and --max-chars at least 40")
    return args


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    try:
        root = resolve_dataset(args.repo, args.cache_dir, args.refresh)
        ranked = [
            (score, path, audit)
            for path, audit in load_audits(root)
            if (score := match_score(args.query, path, audit)) > 0
        ]
        ranked.sort(key=lambda item: (-item[0], str(item[1]).casefold()))
        records: list[dict[str, Any]] = []
        filtered = bool(args.dimension) or args.span_type != "all"
        for _, path, audit in ranked:
            record = build_record(
                root,
                path,
                audit,
                set(args.dimension),
                args.span_type,
                args.max_spans,
                args.max_chars,
            )
            if filtered and not record["spans"]:
                continue
            records.append(record)
            if len(records) >= args.limit:
                break
        payload = {
            "query": args.query,
            "dataset_repository": REPO_URL,
            "dataset_commit": dataset_commit(root),
            "retrieved_at": dt.datetime.now(dt.timezone.utc).isoformat(),
            "license_notice": (
                "System Prompt Index says audits and dimension definitions are free to use with "
                "attribution; prompt text belongs to its respective authors."
            ),
            "results": records,
        }
    except QueryError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2

    if args.format == "markdown":
        sys.stdout.write(as_markdown(payload))
    else:
        json.dump(payload, sys.stdout, ensure_ascii=False, indent=2)
        sys.stdout.write("\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
