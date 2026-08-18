# Lightweight Report and Visualization

Use this reference for any durable teardown report, HTML page, or diagram. Its purpose is to make the result decision-useful and auditable without turning the work into a large analytics project.

## Define the report brief

Before drafting, write four internal lines:

- **Question:** What exact product question must this report answer?
- **Audience:** Who will use it? Default to a product or AI architecture stakeholder when unspecified.
- **Decision:** What should the reader be able to decide, verify, or investigate next?
- **Scope:** Which pages, records, dates, assets, and evidence gaps bound the answer?

Do not expand the scope merely to fill a template.

## Use an answer-first spine

Organize the report in this order unless the user specifies another sequence:

1. Direct answer or one-line architecture summary
2. Three to five decision-useful findings
3. Evidence and interpretation for each finding
4. Contradictions, caveats, and unknowns where they affect the claim
5. Recommended next validation or product action

Each major finding should contain four parts: **claim → evidence IDs → interpretation → implication**. Keep source metadata available through evidence IDs, trace tables, or local links instead of repeating it in every paragraph.

## Choose the smallest useful visual

Use prose or a table when it is clearer. When a relationship genuinely needs a visual, select by analytical job:

| Question | Preferred visual |
|---|---|
| What did the user experience over time? | Three-lane journey or flowchart |
| What states and transitions govern one Agent? | State diagram |
| Who called whom, including wait, failure, or handoff? | Sequence diagram |
| How are entities, versions, and asset references related? | ER diagram |
| How do product layers and services connect? | Layered flowchart or C4-style view |
| What exact evidence supports each conclusion? | Traceability table |

One visual should answer one primary question. Avoid a dashboard, animation, 3D styling, or decorative imagery unless the user explicitly needs it and it adds analytical meaning.

## Give every visual a contract

Before rendering, define:

- the question the visual answers;
- the first thing the reader should notice;
- the reading order;
- the evidence IDs supporting key nodes and edges;
- the branch conditions or edge verbs;
- any caveat that changes interpretation.

Use direct labels instead of requiring the reader to decode a distant legend. Do not rely on color alone. Keep labels legible at a narrow viewport, provide horizontal scrolling for wide tables, and retain a text or table fallback when Mermaid cannot render.

Place a short explanation next to every important visual:

1. **Takeaway** — what it shows.
2. **How to read it** — the intended path or encoding.
3. **Why it matters** — the product decision or risk it supports.

## Keep evidence and caveats visible

- Place evidence IDs beside consequential claims and diagram nodes, not only in an appendix.
- Put a caveat next to the finding it limits.
- Preserve contradictions rather than averaging them into one conclusion.
- Distinguish product fact, inference, recommendation, and unknown in both prose and visuals.
- Never let visual polish imply certainty beyond the underlying evidence.

## Run a lightweight delivery check

Before delivery, verify:

- the first screen answers the report question;
- section titles reveal the reading order;
- major claims include evidence, interpretation, and implication;
- every visual is necessary and has an adjacent explanation;
- labels, tables, legends, and evidence IDs remain usable on desktop and narrow screens;
- Mermaid or other diagrams render, with a readable fallback if they do not;
- HTML navigation and local links work, and the console has no relevant errors;
- private browser state, credentials, and unsupported backend claims are absent.

Stop after the requested artifact. A concise report with a defensible answer is preferable to a comprehensive but weakly evidenced dashboard.
