# Analysis Modes and Deliverable Contracts

Read only the section for the requested mode, plus the shared rules at the end.

## Mode A — User journey

Use when the user asks what people experience from entry to outcome.

### Required evidence coverage

- original requirement, script or content, style and reference assets;
- first product response and every confirmation request;
- what changed after each confirmation;
- continue, modify, choose alternative, interrupt, and go-back affordances;
- normal generation, correction, failure, insufficient balance, interruption;
- chat, task, canvas, history, preview, and editor consistency;
- visible emotion cues and friction, clearly separated from inferred sentiment.

### Delivery order

1. Scope inspected
2. Inaccessible or unconfirmed evidence
3. Evidence table: stage, goal, user action, page feedback, decision, state/asset change, friction, evidence IDs
4. Three-lane journey: `User`, `Product interface`, `System result`
5. Normal, correction, and failure/interruption branches with explicit conditions
6. User emotions, thoughts, friction, and fields the user can supplement
7. Product opportunity points
8. Three highest-value UX questions

Use diamonds for decisions such as satisfied/dissatisfied, success/failure, continue/interrupt, and balance sufficient/insufficient.

## Mode B — Agent inventory and I/O contracts

Use when the user asks how visible Agents collaborate. Do not assume a standard team.

### Identify each Agent

Record name, first appearance, trigger, predecessor, successor, re-entry, and missing-but-expected stages. A UI container or master identity may coordinate Agents, but label that as inference unless routing behavior is visible.

### Six input sources

Classify every input as:

1. User current input
2. User long-term information
3. Project global context
4. Upstream Agent output
5. Platform public assets or knowledge
6. Tool or runtime result

### Observable judgment

Describe only functional decisions: sufficiency checks, next-step selection, confirmation gate, auto-continue rule, stop condition, modification handling, failure handling, completion test, and whether output quality was actually verified.

### I/O contract card

For every evidenced Agent output:

1. Core goal
2. Trigger conditions
3. Inputs, each with source type and requirement status
4. Observable judgments
5. Tools with evidence status
6. Outputs: reply, UI component, structured field, asset, status, downstream task
7. Context read/write table: object, operation, producer, consumer, update timing, evidence class, evidence IDs
8. Completion conditions
9. Exception and retry behavior
10. Unknowns

### Global data-flow audit

Check multiple versions, chat/canvas consistency, stable asset references, downstream invalidation after upstream edits, read-only or write-only fields, and oral completion without committed state.

## Mode C — Functional-equivalent System Prompt

Use for one named Agent only, after its contract is sufficiently evidenced. The goal is behavioral equivalence, not recovery of official text.

### Boundary report

Answer: problem solved, takeover point, trigger, successor, in-scope work, out-of-scope work, modification re-entry, mandatory stops, automatic continuation, and confirmation requirements.

### Contracts

- Input contract: the six source classes from Mode B, with required/optional/unknown.
- Output contract: user replies, interface components, textual/visual/audio/video assets, context writes, status, downstream task.
- Tool contract: preconditions, confirmation, required parameters, success evidence, validation, retry, duplicate-cost risk, interruption behavior, state-write failure.
- State machine: `waiting_input`, `planning`, `waiting_confirm`, `executing`, `validating`, `completed`, `failed`, `interrupted`, `retrying`, `handoff`, adjusted to evidence.

### Rule classes

- `【事实规则】`: directly supported by evidence.
- `【推断规则】`: needed to reproduce observed behavior.
- `【建议规则】`: added for reliability or safety.
- `【未知】`: cannot be decided.

Cover identity, goal, boundary, input checks, context reads/writes, workflow, tool choice, preconditions, confirmation, validation, modification, failure, interruption, handoff, completion, and output format.

### Prompt structure

1. Agent name and role
2. Core objective
3. Task boundary
4. Input contract
5. Global context protocol
6. Workflow
7. Tool-call rules
8. User confirmation mechanism
9. Result validation
10. Modification and rollback
11. Exception handling
12. State machine
13. Downstream handoff
14. Completion conditions
15. Output format

Use placeholders such as `<生成视频工具>` for hidden tool names. Semantic context fields must be labeled as inferred design when the real schema is not exposed.

### Minimum tests

At least: complete input, missing required input, local modification, tool failure, user interruption, and UI/context conflict. Each test specifies input, initial state, expected judgment, expected tool calls, expected state change, and forbidden behavior.

## Mode D — Full product architecture

Use accepted Journey, Agent contract, tool, context, and single-Agent prompt artifacts as inputs. Read [architecture-framework.md](architecture-framework.md).

### Delivery order

1. One-line architecture summary
2. Evidence sources and gaps
3. Core functional domains
4. End-to-end flow table
5. Layered product architecture
6. Agent, tool, and context relationships
7. Global context architecture
8. Knowledge and public assets
9. Model access and routing
10. Technical capability/selection table
11. Entity table and ER diagram
12. End-to-end sequence diagram
13. Product panorama architecture diagram
14. Current architecture (As-Is)
15. Recommended architecture (To-Be)
16. Key risks
17. Component-to-evidence trace table
18. Unknowns

## Shared output rules

- Start with scope and evidence gaps, not certainty theater.
- Keep confirmed, inferred, recommended, and unknown items visibly distinct in tables and diagrams.
- Put evidence IDs in diagram nodes or provide an adjacent mapping.
- Use concrete branch labels and edge verbs: call, read, write, event, confirmation, asset reference, and state update.
- Cite local screenshots and artifacts with clickable paths when available.
- If the user requests HTML, produce a standalone, navigable page and validate it locally.
- End at the requested mode and wait for review when the workflow is staged.
