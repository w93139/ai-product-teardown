# Evidence and Observation Protocol

Use this protocol whenever new product evidence must be collected.

## 1. Scope manifest

Before analysis, record:

| Field | Required content |
|---|---|
| Target | Product, workspace, project, or Space being inspected |
| Time range | Earliest and latest accessible records |
| Surfaces | Chat, canvas, cards, forms, task panel, preview, editor, versions, asset library, model selector, billing, errors |
| Access gaps | Login, hidden history, unavailable preview, missing permissions, unloaded media |
| Mutation boundary | Actions explicitly forbidden and any action specifically authorized by the user |
| External sources | Official sources used, or “none” |

## 2. Evidence source taxonomy

Use one source type per ledger row:

- `USER_ACTION`: visible user message, upload, selection, confirmation, modification, interruption
- `AGENT_MESSAGE`: Agent name plus visible natural-language reply or public planning summary
- `UI_CONTROL`: button, form, selector, option, menu, preview or edit entry
- `TASK_STATE`: pending, running, completed, failed, interrupted, retrying, or other visible status
- `CANVAS_ASSET`: script, character, scene, prop, storyboard, image, video, audio, Face ID, voice, or card
- `ASSET_VERSION`: history entry, prior result, revision, lineage, or replacement
- `TOOL_RESULT`: visible execution result, progress, failure, retry, or asset creation event
- `MODEL_SETTING`: model name, mode, resolution, duration, ratio, or capability shown in UI
- `ERROR_OR_BILLING`: safety block, insufficient balance, cost, credit, refund, or quota notice
- `OFFICIAL_SOURCE`: official page or documentation used to supplement product behavior

## 3. Ledger schema

Create a row for every meaningful observation:

| ID | Sequence | Source type | Surface | Actor/Agent | Exact visible evidence | Asset/state change | Screenshot | Class | Notes/conflict |
|---|---:|---|---|---|---|---|---|---|---|
| E001 | 1 | USER_ACTION | Chat | User | Short quotation or faithful transcription | None | S01 | 已确认 | Earliest visible event |

Use brief quotations; do not copy unnecessarily long proprietary text. Include button labels, model labels, errors, and asset names exactly where they establish behavior.

## 4. Chronological walk

At each event ask:

1. What is the user's immediate goal?
2. What did the user submit, select, confirm, reject, modify, or interrupt?
3. Which Agent or interface responded?
4. What decision or confirmation was requested?
5. What changed in the chat, task state, canvas, history, or assets?
6. Is there visible proof that an execution actually happened?
7. What is the next available user action?
8. What happens on dissatisfaction, failure, insufficient balance, or interruption?

## 5. Cross-surface corroboration

For important transitions, inspect this matrix:

| Claim | Chat | Task state | Canvas/card | History | Preview/actual asset | Result |
|---|---|---|---|---|---|---|
| “Video finished” | Agent says complete | Completed? | Video card exists? | Version recorded? | Plays/opens? | Confirmed, conflict, or unknown |

Do not collapse conflicts. Example: `E021` confirms the Agent claimed completion, while `E022` confirms the asset panel was empty. The product state is therefore contradictory, not complete.

## 6. Confirmation and mutation gates

Identify whether the interface records a confirmation as a durable state or merely receives conversational approval. Investigate separate gates for:

- approving project parameters;
- spending generation credits;
- batch generation;
- overwriting or replacing an accepted asset;
- entering a downstream stage;
- publishing or exporting;
- retrying after a chargeable failure.

Never cross a mutation gate during read-only research.

## 7. Evidence-based tool inference

A tool call is **confirmed** only if a visible result supports execution, such as progress, an execution card, an error, an asset, a version, or a committed state transition. A public Agent plan supports only that the Agent intended the action.

If the official tool name is hidden, use a functional placeholder:

| Functional name | Evidence needed | Label |
|---|---|---|
| `<读取项目上下文>` | Existing project values appear in an Agent response or form | Functional name, not official |
| `<生成角色主图>` | Generation status/result plus character image asset | Functional name, not official |
| `<检查余额>` | Balance check or insufficient-credit error | Functional name, not official |

## 8. Screenshot protocol

- Use stable IDs such as `S01`, `S02` and map them to filenames or URLs.
- Capture enough surrounding interface to identify the surface and state.
- Record what the screenshot proves; filenames are not proof if their label conflicts with visible content.
- Avoid sensitive identity, billing, or credential details. Redact only when needed and disclose the redaction.
- When media quality matters, inspect the actual preview if safe and already generated.

## 9. Completion audit

Before delivery, confirm that:

- conclusions are labeled;
- every critical table row has evidence;
- all diagram nodes are traced;
- unavailable surfaces are listed;
- contradictory states remain explicit;
- normal, modification, failure, balance, interruption, and retry paths are included only to the extent supported;
- product claims are not substituted for observed behavior;
- no hidden prompt, chain-of-thought, backend implementation, or official API name was invented.
