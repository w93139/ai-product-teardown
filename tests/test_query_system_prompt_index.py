from __future__ import annotations

import importlib.util
import json
from pathlib import Path
import tempfile
import unittest


SCRIPT = Path(__file__).parents[1] / "scripts" / "query_system_prompt_index.py"
SPEC = importlib.util.spec_from_file_location("query_system_prompt_index", SCRIPT)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class QuerySystemPromptIndexTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        (self.root / "audits" / "Acme").mkdir(parents=True)
        (self.root / "prompts" / "Acme").mkdir(parents=True)
        (self.root / "dimensions.json").write_text('{"categories": []}', encoding="utf-8")
        audit = {
            "id": "Acme/Acme-Agent-2026",
            "company": "Acme",
            "product": "Acme Agent 2026",
            "category": "coding-agents",
            "annotation": "human",
            "protective_entries": 1,
            "problematic_entries": 1,
            "by_dimension": {},
            "spans": [
                {
                    "text": "Ask before deleting files.",
                    "start": 0,
                    "end": 25,
                    "dimension": "D4",
                    "score": 1,
                    "note": "Preserves control over destructive actions.",
                    "risky": False,
                },
                {
                    "text": "Do not ask clarifying questions.",
                    "start": 26,
                    "end": 58,
                    "dimension": "D5",
                    "score": -1,
                    "note": "May reduce user agency.",
                    "risky": True,
                },
            ],
        }
        path = self.root / "audits" / "Acme" / "Acme-Agent-2026.json"
        path.write_text(json.dumps(audit), encoding="utf-8")
        (self.root / "prompts" / "Acme" / "Acme-Agent-2026.md").write_text(
            "Published prompt body", encoding="utf-8"
        )

    def tearDown(self) -> None:
        self.temp.cleanup()

    def test_match_and_provenance(self) -> None:
        audits = list(MODULE.load_audits(self.root))
        self.assertEqual(len(audits), 1)
        path, audit = audits[0]
        self.assertGreater(MODULE.match_score("Acme Agent", path, audit), 0)
        record = MODULE.build_record(self.root, path, audit, set(), "all", 8, 600)
        self.assertEqual(record["annotation"], "human")
        self.assertEqual(record["risky_entries"], 1)
        self.assertTrue(record["audit_url"].endswith("audits/Acme/Acme-Agent-2026.json"))
        self.assertTrue(record["prompt_url"].endswith("prompts/Acme/Acme-Agent-2026.md"))

    def test_dimension_and_span_type_filters(self) -> None:
        _, audit = next(iter(MODULE.load_audits(self.root)))
        spans = MODULE.select_spans(audit, {"D5"}, "problematic", 8, 600)
        self.assertEqual([span["dimension"] for span in spans], ["D5"])
        risky = MODULE.select_spans(audit, set(), "risky", 8, 600)
        self.assertEqual(len(risky), 1)
        self.assertTrue(risky[0]["risky"])

    def test_output_never_contains_full_prompt_body(self) -> None:
        path, audit = next(iter(MODULE.load_audits(self.root)))
        record = MODULE.build_record(self.root, path, audit, set(), "all", 8, 600)
        rendered = json.dumps(record)
        self.assertNotIn("Published prompt body", rendered)

    def test_span_text_and_note_are_bounded(self) -> None:
        _, audit = next(iter(MODULE.load_audits(self.root)))
        audit["spans"][0]["note"] = "x" * 100
        spans = MODULE.select_spans(audit, {"D4"}, "all", 8, 40)
        self.assertEqual(len(spans[0]["note"]), 40)
        self.assertTrue(spans[0]["truncated"])


if __name__ == "__main__":
    unittest.main()
