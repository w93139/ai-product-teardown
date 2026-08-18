---
name: ai-product-teardown
description: Reverse-engineer an AI product from authenticated UI evidence, producing traceable user journeys, Agent I/O contracts, functional-equivalent prompts, or layered product architecture. Use for read-only product teardowns grounded in chats, canvases, assets, states, errors, and official sources; do not use for generic market research based only on promotional pages.
metadata:
  version: "2.0.0"
---

# AI Product Reverse Engineering

Turn observable product behavior into a defensible product model. Preserve the boundary between what the interface proves, what behavior suggests, what should be designed, and what remains unknown.

## Choose the requested depth

Select only the mode needed by the user. Do not silently continue into later modes.

1. **Journey** — reconstruct what the user does, sees, decides, corrects, and experiences.
2. **Agent contracts** — identify only Agents that visibly appear, then map input, observable judgment, tools, output, context reads/writes, and handoff.
3. **Functional-equivalent prompt** — for one named Agent, convert its evidenced behavior into an implementable specification and System Prompt without claiming access to proprietary wording or hidden reasoning.
4. **Architecture** — combine accepted earlier artifacts into end-to-end flows, layers, data entities, state, asset, model, billing, safety, and infrastructure views.
5. **Full teardown** — run the four modes in order, pausing for user confirmation between them when the user requests staged validation.

Read [analysis-modes.md](references/analysis-modes.md) for the selected mode. For Architecture mode, also read [architecture-framework.md](references/architecture-framework.md). For any durable report, HTML page, or diagram, read [report-and-visualization.md](references/report-and-visualization.md). For HTML delivery, also read [html-delivery.md](references/html-delivery.md) and reuse [report-template.html](assets/report-template.html) when it helps.

For a staged teardown, multi-artifact delivery pack, or team handoff with explicit acceptance gates, also read [staged-execution-sop.md](references/staged-execution-sop.md). It coordinates artifact dependencies, accepted versions, and mode transitions; it does not replace the selected mode contract or require earlier modes when the user requested only one mode.

## Operate within the evidence boundary

- Treat the product as read-only unless the user explicitly authorizes a specific mutation.
- Do not send product messages or trigger generation, regeneration, batch generation, publishing, deletion, purchase, recharge, export with side effects, or asset overwrite.
- Safe inspection may include scrolling history, expanding public planning summaries, switching visible asset categories, opening existing previews, and reading existing version or error panels.
- If authentication, CAPTCHA, or manual takeover is required, stop and let the user take control. Never inspect or expose cookies, tokens, passwords, authorization headers, private browser storage, or sensitive identity data.
- Use the current signed-in session only through an available browser-control capability. Do not bypass access controls.
- If external research is necessary, restrict factual supplementation to the product's official site or official documentation. Never elevate third-party speculation to product fact.
- Do not claim access to hidden chain-of-thought, private prompts, internal tool names, backend languages, databases, queues, clouds, or vendor contracts unless directly evidenced.

Read [evidence-and-observation.md](references/evidence-and-observation.md) before collecting new evidence.

## Maintain one evidence ledger

Assign stable evidence IDs such as `E001`, `E002`, and `E003` in chronological order. Every consequential claim, diagram node, and key edge must cite one or more IDs.

Use exactly these conclusion classes unless the user specifies equivalent labels:

- **【已确认】** — directly visible in the product, official material, or a reproducible read-only result.
- **【合理推断】** — multiple facts support the behavior, but the implementation is not visible.
- **【建议设计】** — a proposed improvement, never represented as current behavior.
- **【未知】** — evidence is insufficient or contradictory.

In Journey mode, `【页面事实】` is an acceptable user-facing alias for `【已确认】`, and `【尚未确认】` for `【未知】`.

For every ledger entry capture: source type, visible text or control, Agent identity if shown, asset or status observed, screen or screenshot ID, sequence position, and confidence class. Preserve conflicting observations as separate entries.

## Apply the verification invariants

These rules prevent the most common false conclusions:

- An Agent saying “completed” is conversation evidence, not proof that an asset exists or the task state committed.
- An Agent describing a plan is not proof of a tool call. Confirm execution only through a tool result, asset change, status transition, history entry, or other visible result.
- A tool reporting success is not proof that the UI, context, and asset store agree.
- “Meets requirements” is not quality validation. Inspect the output against script, duration, style, identity consistency, references, dialogue, and requested format when those are visible.
- Chat, canvas, task panel, history, preview, and asset library are independent evidence surfaces. Record disagreement; never choose one silently as the truth.
- Do not assume a fixed number of Agents, tools, fields, models, or workflow stages. Record only evidenced instances, then mark structural additions as inference or recommendation.
- When an upstream entity changes, explicitly investigate whether downstream assets were invalidated, versioned, recomputed, or left stale.

## Execute the teardown

1. **Frame the scope.** Record the target product or project, requested mode, accessible surfaces, time range, and prohibited actions.
2. **Inventory sources.** List user actions, conversation records, Agent labels, forms and buttons, canvas assets, versions, model selectors, tool results, statuses, errors, billing indicators, and official sources.
3. **Walk chronologically.** Start at the earliest accessible event. Track triggers, decisions, confirmations, corrections, failures, interruptions, asset changes, and handoffs.
4. **Cross-check surfaces.** For each claimed transition compare chat, canvas, task state, history, and actual preview or asset existence.
5. **Distill the answer.** State the decision-useful conclusion first, then organize only the findings, evidence, caveats, and next actions needed to support it.
6. **Build the selected artifact.** Use the relevant contract and table schemas from the mode reference. Keep facts, inference, recommendations, and unknowns visibly separate.
7. **Use the smallest useful visual.** Add a table or diagram only when it makes a relationship easier to understand than prose. Define its question and reading path before rendering it.
8. **Trace diagrams back to evidence.** Put evidence IDs in nodes or an adjacent trace table. Label branch conditions and edge semantics.
9. **Audit completion.** Check coverage of normal, correction, failure, insufficient balance, interruption, retry, and state-conflict paths when evidence exists.
10. **Render and verify.** If delivering HTML, test it locally, verify navigation and Mermaid rendering, check console errors, and inspect desktop and narrow viewports.
11. **Stop at the requested boundary.** Report inaccessible evidence and unresolved questions. Do not proceed into prompt reconstruction or architecture unless requested.

## Make implementation boundaries explicit

- Name a tool functionally when the official name is not visible, for example `<生成视频工具>`, and label it “功能命名，非官方工具名”.
- Summarize observable functional judgments, not internal reasoning steps.
- Treat context field names as semantic placeholders when the UI does not expose a schema.
- Separate current architecture (**As-Is**) from inferred implementation and recommended architecture (**To-Be**).
- For databases, queues, model gateways, storage, and clouds, state required capabilities first; list possible or recommended options only under inference or recommendation.
- Put safety and billing enforcement in deterministic service boundaries in recommended designs; prompts may explain rules but should not be the sole enforcement layer.

## Quality bar

A finished teardown must let another reviewer answer:

- What did the user submit and confirm?
- Which visible Agent or interface component handled each step?
- What changed in chat, state, and assets?
- What evidence proves a tool or model action occurred?
- How are upstream assets referenced and reused downstream?
- Where can the user modify, retry, interrupt, or return?
- Where can balance, safety, or model limits stop execution?
- Which claims are fact, inference, recommendation, or unknown?
- Why might chat and canvas disagree, and what would make completion authoritative?

Prefer a concise, evidence-dense artifact over a long narrative. Preserve screenshot links and local artifact links so the user can audit the result.
