# Product Architecture Framework

This is an analysis template, not a claim that the target product uses these component or table names.

## 1. Five simultaneous end-to-end flows

Trace one complete project across:

1. **User interaction flow** — entry, input, selection, confirmation, modification, interruption, preview, export.
2. **Agent control flow** — router or visible Agent, specialist trigger, confirmation gate, handoff, re-entry.
3. **Tool-call flow** — context operations, parsing, generation, safety, billing, storage, validation.
4. **Data/context flow** — read fields, decisions, writes, versions, references, confirmations, errors.
5. **Media asset flow** — source uploads, images, Face ID, views, audio, video, composition, preview, versions.

For each step record trigger, handler, reads, judgment, call, result, state write, confirmation, successor, and failure branch.

## 2. Layered architecture checklist

Do not force an empty layer into the confirmed architecture.

1. **User and channel** — account, permission, membership, balance, preferences, private library, project history, sharing.
2. **Interaction/workbench** — chat, Agent identity, canvas, cards, forms, buttons, task panel, preview, editor, history, errors.
3. **Product application** — project, script, character, scene, prop, storyboard, video, audio, asset, version, publishing management.
4. **Agent and workflow orchestration** — controller, specialists, trigger rules, state machine, confirmation, handoff, interrupt, rollback, retry, idempotency, completion gates.
5. **Tools and services** — context read/write, parsing/extraction, prompt preparation, media generation, composition, preview/export, safety, balance, billing, storage.
6. **Model access and routing** — text, image, video, audio/TTS; capabilities, constraints, cost, latency, failure, fallback, retry.
7. **Global context and data** — user, project, script, entities, storyboards, references, Agent runs, tool calls, confirmations, state, versions, errors, billing, feedback.
8. **Knowledge and public assets** — style library, templates, film grammar, prompt templates, model capability knowledge, safety/copyright/billing rules, public/private isolation.
9. **Infrastructure and governance** — auth, authorization, structured storage, object storage/CDN, async jobs, queue, model gateway, logs/traces, evaluation, safety, cost controls, versioning, privacy.

## 3. Structured global context

Use these semantic slices when useful. Mark each one confirmed, inferred, recommended, or unknown; never present these labels as actual backend field names without evidence.

| Slice | Typical content | Invalidation concern |
|---|---|---|
| UserContext | user, language, membership, quota, preferences, private assets | permission and tenant changes |
| ProjectConfig | format, aspect ratio, dialogue language, style, model settings | broad downstream impact |
| ScriptContext | source script, structured script, version | storyboard, dialogue, duration |
| CharacterContext | identity, reference, Face ID, main image, multi-view, voice | storyboards, image/video shots, audio |
| SceneContext | descriptions, main image, multi-view | referenced storyboards and videos |
| PropContext | descriptions and image assets | referenced storyboards and videos |
| StoryboardContext | shot description, entity references, camera language, prompts | generated media and edit timeline |
| AssetContext | image/video/audio URI, metadata, status, lineage, version | preview and downstream references |
| WorkflowState | current Agent, task, confirmation, error, interrupt, retry | all control decisions |
| BillingContext | estimate, reservation, consumption, refund | chargeable execution gates |
| EvaluationContext | automated checks, user feedback, failure reason | retry, routing, product learning |

Prefer stable IDs and versioned references over copied descriptive text. A downstream asset should record which upstream versions produced it.

## 4. Knowledge architecture questions

Separate project data from reusable knowledge.

- **Style execution:** Does a user-facing style choice map to prompt tokens, reference images, model parameters, or a versioned style profile?
- **Identity reuse:** Is a character represented by stable ID, Face ID, reference set, embeddings, multi-view assets, or copied prompts?
- **Film grammar:** Is camera knowledge visible in prompts, templates, specialist behavior, or official documentation?
- **Model capabilities:** What source of truth defines duration, resolution, aspect ratio, reference support, safety, cost, and availability?
- **Policy enforcement:** Safety and billing may be described in prompts, but deterministic services should enforce them.
- **Feedback:** Does feedback update only the project, a user preference, an evaluation dataset, or routing policy?
- **Isolation:** Are user private assets permissioned and tenant-scoped separately from platform public assets?

## 5. Model access and routing

Do not infer dynamic routing from one visible model selector. Distinguish:

- directly exposed model or mode;
- inferred model gateway required by behavior;
- recommended capability registry and policy router.

For each model class track task fit, input/reference constraints, duration, resolution, cost, latency, failure modes, safety limitations, fallback policy, and evidence. Model capability changes should be versioned and independently enforceable from Agent prompts.

## 6. Technical selection table

For every invisible backend component output:

| Capability needed | Page evidence | Possible approach | Recommended design | Why implementation is unconfirmed |
|---|---|---|---|---|

Cover workbench front end, Agent orchestration, durable state machine, async execution, model gateway, tool invocation, context store, business database, object storage/CDN, asset versioning, queue, confirmation and interrupt, credit reservation, content safety, logs/traces, model evaluation, knowledge retrieval, and tenant isolation.

Vendor, language, database, queue, or cloud names belong only under possible or recommended approaches unless officially evidenced.

## 7. Core entity template

Consider: User, Project, Conversation, Agent, AgentRun, Workflow, Task, ToolCall, Script, Character, Scene, Prop, Storyboard, Asset, AssetVersion, UserConfirmation, ModelInvocation, Error, BillingRecord, and Feedback.

These are semantic analysis entities, not asserted table names. Record relationship, cardinality, versioning, evidence, and inference status. Key relationships include:

- Project owns context and workflow instances.
- Conversation events may trigger AgentRuns.
- AgentRun reads versioned inputs and creates Tasks or ToolCalls.
- Storyboard references stable Character, Scene, and Prop versions.
- ToolCall or ModelInvocation produces AssetVersions.
- Confirmation gates a version or transition.
- BillingRecord links to a chargeable invocation and idempotency key.
- Error and Feedback attach to runs, assets, or evaluations.

## 8. Sequence and panorama diagrams

The sequence diagram should show: input, parameter confirmation, context write, Agent call, tool call, asynchronous wait, asset write-back, user confirmation, modification, failure, interruption, and downstream handoff.

The panorama should:

- place each layer in one subgraph;
- label arrows with `调用`, `读取`, `写入`, `事件`, `确认`, `资产引用`, or `状态更新`;
- use solid lines for confirmed relations;
- use dashed lines for inference;
- use a distinct color or heavy/dotted style for recommendations;
- mark state conflicts, missing validators, and unreliable completion gates;
- include a legend and a component-to-evidence trace table.

## 9. As-Is, To-Be, and risk audit

Audit whether the recommended architecture needs:

- a single authoritative state source;
- asset existence and context-commit completion gates;
- duration, style, identity, dialogue, and audiovisual-sync validation;
- a versioned asset dependency DAG and invalidation rules;
- idempotent retries and duplicate-charge prevention;
- cost estimate, quota check, reservation, settlement, and refund;
- interrupt propagation to queued and running jobs;
- full trace IDs across Agent, tool, model, asset, state, and billing;
- model capability registry and routing evaluation;
- project-local feedback versus durable user preference separation;
- tenant-scoped private asset authorization.

Prioritize risks by user harm and irreversibility: state conflicts, false completion, lost asset writes, stale downstream assets, duplicate billing, major duration mismatch, missing quality validation, safety false positives, post-interrupt execution, private-asset leakage, stale knowledge, and model-policy drift.
