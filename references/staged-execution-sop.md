# Staged Teardown Execution and Acceptance SOP

Use this reference only for a staged teardown, a multi-artifact delivery pack, or a team workflow that needs explicit acceptance and handoff between modes. For a single Journey, Agent contract, prompt, or Architecture request, use the relevant section of [analysis-modes.md](analysis-modes.md) without imposing this full sequence.

This SOP coordinates existing mode contracts. It does not replace the evidence rules in [evidence-and-observation.md](evidence-and-observation.md), the architecture model in [architecture-framework.md](architecture-framework.md), or the delivery rules in [report-and-visualization.md](report-and-visualization.md).

## 1. Preserve one dependency chain

Treat the outputs as a dependency graph, not four unrelated reports:

```text
Scope manifest + evidence ledger
        |
        v
Journey baseline
        |
        v
Agent contracts + tool/context maps
        |
        v
One-Agent functional-equivalent prompt
        |
        v
Product architecture (As-Is / To-Be)
```

- Maintain one chronological evidence ledger with stable IDs such as `E001`, `E002`, and `E003` across all artifacts. Add a `Stage` column when filtering by mode; do not renumber the same evidence in each report.
- Record the accepted artifact version used by the next stage. Never silently use a superseded draft.
- Carry unresolved conflicts and unknowns forward. Acceptance means the artifact is suitable as an input, not that every unknown has been resolved.
- A downstream artifact may reinterpret evidence, but it must not silently alter an accepted upstream fact.

## 2. Choose the execution shape

| User request | Execution shape |
|---|---|
| One named mode | Run that mode only. List missing upstream inputs as evidence gaps. |
| Architecture only | Audit available Journey, contract, context, and tool evidence; proceed with an explicitly bounded architecture if sufficient. Do not silently generate full earlier reports. |
| Full teardown without requested checkpoints | Run the needed modes in order and make mode boundaries visible, but do not stop for confirmation unless a choice would materially change scope. |
| Staged validation or course/review workflow | Stop at each requested gate and wait for acceptance before using that artifact downstream. |
| Multi-person or multi-agent delivery | Use the handoff record below so each contributor receives the same accepted evidence baseline. |

If a stage lacks enough evidence, deliver the supported subset plus a gap list. Do not fill the gap with template components or familiar industry patterns.

## 3. Create the shared control artifacts

Before the first substantive mode, create or update these lightweight records:

### Scope manifest

Record target, accessible time range, surfaces, access gaps, mutation boundary, official sources, requested modes, expected deliverables, and requested review gates.

### Artifact register

| Artifact | Version | Status | Evidence range | Accepted by/at | Downstream consumers | Open conflicts |
|---|---|---|---|---|---|---|
| Journey | v0.1 | draft/accepted/superseded | E001-E0xx |  | Agent contracts |  |

Use `accepted` only after the requested reviewer accepts it or, when no checkpoint was requested, after the completion audit passes. Use `superseded` rather than overwriting an accepted version when a material factual baseline changes.

### Stage handoff record

Each transition should state:

1. accepted input artifacts and versions;
2. evidence IDs newly added in the stage;
3. confirmed conclusions carried forward;
4. unresolved conflicts and unknowns;
5. user decisions or scope changes;
6. prohibited actions that remain in force;
7. exact next-mode question.

## 4. Apply the stage gates

Use only the gates relevant to the requested execution shape.

### Gate 0 — Evidence readiness

Pass when:

- scope and mutation boundary are explicit;
- accessible surfaces and gaps are listed;
- the earliest accessible event and current state are identifiable;
- the evidence ledger and screenshot naming scheme are established;
- no credential, private browser state, or unauthorized mutation is required.

If this gate fails, report the safe subset that can still be inspected and the minimum material or authorization needed to continue.

### Gate 1 — Journey accepted as behavioral baseline

Pass when:

- the timeline has no unexplained material gap within the accessible range;
- user actions, interface responses, and system/asset results are separated;
- important completion claims are cross-checked against task, canvas, history, and preview where available;
- normal, correction, failure, balance, interruption, and retry paths are included only to the extent evidenced;
- the Journey states what an Agent-contract analysis may safely treat as an observed transition.

Do not infer hidden Agent responsibilities merely to close the Journey.

### Gate 2 — Agent contracts accepted as implementation input

Pass when:

- every listed Agent has visible identity or an explicitly labeled functional identity;
- trigger, predecessor, successor, re-entry, inputs, outputs, context reads/writes, tools, and completion conditions are traceable;
- planned tool use is separated from visibly executed behavior;
- producers, consumers, versions, and invalidation concerns are recorded for important data and assets;
- unsupported Agents and tools remain outside the As-Is contract.

The accepted contract becomes the source of truth for a functional-equivalent prompt. Later prompt design must not expand the Agent's evidenced ownership without labeling the addition as recommendation.

### Gate 3 — Functional-equivalent prompt accepted for one Agent

Pass when:

- the target Agent and boundary are unambiguous;
- every consequential rule is classified as fact, inference, recommendation, or unknown;
- confirmation, chargeable action, overwrite, interruption, retry, validation, and handoff behavior are explicit;
- completion requires observable asset/state/context agreement rather than the Agent's own completion message;
- the minimum tests cover complete input, missing input, modification, tool failure, interruption, and UI/context conflict;
- hidden official wording, chain-of-thought, schemas, and tool names are not claimed.

Acceptance validates behavioral implementability, not identity with the vendor's private prompt.

### Gate 4 — Architecture accepted as a traceable product model

Pass when:

- the five end-to-end flows align on the same representative task;
- every As-Is component and key edge has evidence or is visibly classified as inference/unknown;
- template layers are omitted from confirmed architecture when no evidence supports them;
- context slices show producers, consumers, versions, references, and invalidation concerns;
- As-Is and To-Be are independently readable;
- recommended safety, billing, state, retry, and governance controls sit in deterministic service boundaries where appropriate;
- the component-to-evidence trace table covers the main diagram and material claims.

## 5. Control change across stages

When new evidence contradicts an accepted artifact:

1. append the new observation to the ledger with a new evidence ID;
2. preserve both observations and describe the conflict;
3. identify affected claims, contracts, prompt rules, diagrams, and recommendations;
4. create a new artifact version for material changes;
5. mark the prior version `superseded`, not deleted;
6. re-run only the affected gates and downstream artifacts.

Use a dependency table for non-trivial changes:

| Changed item | Directly affected | Possible downstream impact | Required action |
|---|---|---|---|
| Character version | Storyboard references | Image/video assets and preview | Check invalidation, lineage, and local recompute |

Do not restart the entire teardown when a bounded revision can be traced and revalidated.

## 6. Normalize recovery decisions

| Condition | Preserve | Verify before retry/continuation | Stop condition |
|---|---|---|---|
| Generation failure | input, task ID, error, partial assets | charge, duplicate task, retry affordance, state write | retry would mutate or charge without authorization |
| Insufficient balance | estimate, balance notice, task state | whether any reservation or charge occurred | recharge or paid retry is required |
| Safety block | exact visible message and blocked stage | product rule vs model response only when evidenced | bypass or sensitive probing would be required |
| User interruption | completed/partial work and timestamps | queued/running jobs, later assets, later charges | user has not authorized resumption |
| State-write failure | tool result and asset separately | idempotency and current authoritative state | retry could duplicate an asset or charge |
| Cross-surface conflict | all contemporaneous surface observations | timestamps, versions, actual preview | read-only evidence cannot resolve the conflict |
| Downstream start failure | handoff payload and upstream result | missing dependency and downstream task state | upstream cannot honestly claim full completion |

These rows guide analysis; they do not authorize triggering the failure or retry path.

## 7. Package only what the user needs

For a formal multi-artifact delivery, a useful minimal package is:

```text
teardown/
|-- 00-scope-and-evidence.md
|-- 01-journey.md
|-- 02-agent-contracts.md
|-- 03-<agent>-functional-prompt.md
|-- 04-product-architecture.md
|-- evidence/
|   |-- ledger.md
|   `-- screenshots/
`-- delivery-manifest.md
```

Adapt names and formats to the user's request. Do not create empty placeholder reports, a README, or a ZIP merely because this example includes a package.

The delivery manifest should list artifact versions, evidence snapshot time, accepted/superseded status, unresolved conflicts, and any files that depend on network rendering.

## 8. Final cross-artifact audit

Before declaring a staged teardown complete, verify:

- one evidence ID refers to the same observation everywhere;
- Journey transitions match Agent triggers and handoffs;
- prompt ownership matches the accepted Agent contract;
- architecture producers and consumers match the contract/context tables;
- modifications propagate through versions and invalidation rules;
- completion semantics agree across chat, task, asset, context, and preview;
- unknowns were not converted into facts downstream;
- recommendations answer observed risks rather than merely making the architecture look complete;
- the package contains only requested, populated, auditable artifacts.

Completion means the requested artifacts form a consistent, evidence-traceable model. It does not mean inaccessible implementation details have been recovered.
