# Autonomous Screenshot Acquisition

Use this protocol only when new screenshots are needed. It supplements the evidence ledger and mutation boundaries in [evidence-and-observation.md](evidence-and-observation.md); it does not authorize actions that the user or the main skill has prohibited.

## 1. Select the safest available capture path

1. **Web product:** Prefer an available browser-control capability that can reuse the current signed-in session. Use it for safe navigation, inspection, and screenshots.
2. **Mini app or simulator:** Use an available simulator or local app-control capability plus window screenshots. If login, device approval, or unreliable automation requires manual takeover, pause for the user.
3. **Desktop app:** Use available local app control and window-level screenshots. Treat coordinate-based automation as fragile; verify every resulting state and request manual takeover for consequential or ambiguous actions.
4. **User-supplied screenshots:** Do not operate the product. Validate and inventory the supplied files directly.
5. **No suitable control or capture capability:** State the missing capability and ask for screenshots or manual takeover. Do not fabricate evidence from promotional pages.

Browser or app control enables observation, not mutation. Without explicit authorization, do not send messages, submit forms, trigger generation or regeneration, change saved settings, publish, export with side effects, delete, overwrite, purchase, recharge, retry a chargeable task, or deliberately induce failures. Safe inspection may include scrolling, switching existing tabs or asset categories, expanding visible history, and opening an already-created preview when these actions do not alter product state.

## 2. Plan evidence coverage

Before capturing, list the accessible surfaces and the states needed for the requested analysis. Prefer existing evidence of:

- entry and project context;
- user input and visible configuration;
- confirmations and branch controls;
- Agent identity, public planning summaries, and replies;
- task, canvas, asset, history, preview, and version states;
- existing failure, interruption, retry, safety, or insufficient-balance states;
- visible model and billing settings when relevant and non-sensitive.

Do not manufacture missing branches. Record them as access gaps or unknowns.

## 3. Capture only after state verification

For each safe navigation or observation step:

1. Record the intended action and expected evidence surface.
2. Perform only the authorized action.
3. Wait for observable stability: the relevant URL, title, control, status, asset, or loading indicator must reach the intended state.
4. Compare the current state with the prior state. If nothing material changed, determine whether the action failed or the intended evidence was already visible.
5. Capture enough surrounding interface to identify the product surface, Agent or actor, and state.
6. Re-open or visually inspect the saved screenshot. Confirm that visible content—not the filename—proves the intended observation.
7. If the capture shows an unresponsive, loading, blank, obstructed, or wrong state, wait or navigate safely and recapture. Keep an in-progress state only when that state itself is evidence.
8. Add the screenshot to the evidence ledger immediately; do not rely on memory after a long browsing session.

Never treat a loading screenshot as proof of completion. For a long-running task that was already in progress, observe rather than restart it, and capture the final state only if it becomes visible without a new mutating action.

## 4. Protect sensitive information

- Prefer a window or element capture over a full desktop capture.
- Exclude unrelated tabs, notifications, account menus, personal identifiers, private URLs, billing details, and other workspaces.
- Never expose cookies, tokens, passwords, authorization headers, browser storage, developer-tool secrets, or private keys.
- If redaction is necessary, preserve an unmodified private source only when the user has authorized local retention; create a redacted working copy and disclose what category was redacted.
- Do not upload captured evidence to external services unless the user explicitly authorizes that destination.

## 5. De-duplicate without losing state changes

- Compare each new capture with earlier captures using visual inspection; file hashes may be used only as a fast first pass.
- Remove exact duplicate frames from the delivery set.
- Preserve visually similar frames when they prove a meaningful difference such as a new task status, asset card, version, error, balance gate, or changed control state.
- When two screenshots conflict, retain both and record the timestamps or sequence positions and the conflict in the evidence ledger.

## 6. Name and inventory captures

Use stable screenshot IDs in the evidence ledger and descriptive filenames:

```text
S01-<stage>-<action-or-state>.png
S02-<stage>-<action-or-state>.png
```

When producing a durable or multi-artifact report, create a screenshot manifest such as `图片清单.csv` or `screenshot-manifest.csv`:

```csv
id,filename,sequence,action_or_state,surface,validation,evidence_ids,notes
S01,S01-home-project-entry.png,1,Open existing project,Project home,Verified,E001,
```

The manifest must reflect visible content. A filename or planned step is not evidence when the screenshot shows something else.

## 7. Report acquisition results

At the end of collection, report:

- capture method and product platform;
- number of retained screenshots and duplicates removed;
- surfaces and branches covered;
- screenshots that required redaction;
- inaccessible, unsafe, or unconfirmed states;
- any manual takeover performed by the user;
- whether the evidence is sufficient for the requested analysis mode.

Proceed only to the analysis mode requested by the user. Autonomous acquisition does not authorize a full teardown when the user requested only screenshots or one analysis mode.
