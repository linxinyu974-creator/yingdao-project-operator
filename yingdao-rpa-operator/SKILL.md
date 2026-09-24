---
name: yingdao-rpa-operator
description: This skill should be used when the user asks to "operate 影刀", "run a ShadowBot app", "develop a CodeFlow", "inspect an RPA workflow", "debug 影刀", "迁移影刀应用", "验证影刀结果", or asks to manage local 影刀 tasks, Studio flows, browser profiles, exports, credentials, or runtime evidence.
version: 0.1.0
---

# Yingdao RPA operator

Operate Windows 影刀/ShadowBot applications through the real local client, Studio, CodeFlow sources, browser profile, and output files. Keep platform operations, application code, business-page state, and result evidence as separate layers. Use deterministic checks before making a change and report what was observed, changed, saved, published, run, and verified.

This skill consolidates the official `shadowbot-cli` command discipline, community robot-management and XBot API references, and the local `yingdao-project-operator` evidence rules. It does not assume an enterprise API key, a fixed installation path, a fixed user directory, or a particular app architecture.

## Route the request

Classify the request before touching the client.

| Request | Required path |
|---|---|
| Inspect, explain, audit, or compare | Read-only discovery; do not open, log in, run, or mutate an app as a side effect. |
| Edit Python, CodeFlow, selectors, or visual blocks | Identify app, flow, actual call chain, and loaded source; make the smallest authorized edit; save/compile and read back. |
| Run an application or task | Preflight account, client, app, startup flow, running tasks, quota evidence, input files, and output directory; run only the requested surface. |
| Diagnose a failure | Preserve the original error and layer it as CLI, Studio, runtime, browser/profile, business page, file, or data contract. Trace the first failed dependency. |
| Migrate or deliver | Copy only the requested runtime files, rewrite absolute references and dependent hashes, preserve business binaries, and verify the destination before claiming delivery. |
| Build visual blocks or use a cloud API | Load the optional references and verify the current schema. Do not install or invoke an unrelated community tool automatically. |

When the app, flow, account, execution surface, or date range is ambiguous, inspect available local evidence first and ask only for the missing decision that blocks safe progress.

## Establish the local contract

Discover the CLI instead of assuming `D:\ShadowBot` or a particular user UUID. Run the bundled read-only probe when possible:

```powershell
python scripts/operator_probe.py
python scripts/operator_probe.py --live
```

For direct commands, use the discovered executable and quote Windows paths:

```powershell
$env:SWITCH_STUDIO_MCP_CLI_SUPPORT='1'
& $cli system health
& $cli system state
& $cli auth current
```

Interpret `health`, `auth`, and `state` independently. A healthy local endpoint does not prove an authenticated account. An authenticated 影刀 account does not prove the target website is logged in. `hasRunningTask`, `hasStudioOpened`, and `isStudioBusy` may be absent; report unknown rather than false.

If CLI help and a returned schema disagree, stop repeating the wrapper command. Read the current local MCP `tools/list` schema and call only the discovered tool with its exact arguments. Do not bypass disabled tools, permission errors, approval gates, or login requirements. See `references/cli-mcp-and-runtime.md`.

## Inspect before editing

Find the real app ID and type, then identify the startup flow and the execution chain:

```powershell
& $cli console app --search $name --page 1 --page-size 20
& $cli console app detail --app-id $appId
& $cli studio current get
& $cli studio open --app-id $appId
& $cli studio app get
& $cli studio flow list
& $cli studio codeflow read --flow-id $flowId
```

Read all relevant CodeFlow content, visual blocks, parameters, globals, package metadata, and imports. Trace `main` or the configured startup flow through `process.run`, module calls, selectors, browser creation, file preparation, and notification code. Do not infer behavior from a flow name, comment, or a successful empty run.

For Python CodeFlows, confirm the application interpreter and dependencies. A system Python import or `py_compile` result does not prove the 影刀 runtime can import the module. For visual blocks, read the real prototype and form schema before inserting or filling blocks. For selectors, distinguish exploration-session storage from application selector persistence.

## Make and apply changes

Prefer a unique local edit or an exact CodeFlow replacement. Do not overwrite an unread source file to conceal unknown changes. Keep secrets, cookies, CAPTCHA values, full account credentials, and production business files out of source, logs, skill references, and reports.

Use this evidence chain for an authorized edit:

1. Read the current source/flow and record the target.
2. Apply the smallest change.
3. Read back the changed source/flow and compare it with the intended content.
4. Save and compile in Studio.
5. Read diagnostics and confirm no unsaved changes.
6. Verify the loaded/deployed copy if the change is outside the Studio editor.
7. Run only the requested test surface and inspect the actual business artifact.

Saving is local compilation. It is not publishing, synchronization to another computer, or proof that the console entrypoint uses the changed flow. Use `studio current sync` only when closing/synchronizing the current editing session is explicitly required.

## Run with evidence

Before a real run, check the current task state and record the quota gate when available. If a task already exists, observe its status and logs; do not submit a duplicate because a wait timed out. If an explicit quota denial occurs, stop retries until reset.

Choose the execution surface precisely:

- `console task run --app-id` proves an entire application entrypoint.
- `studio app run --flow-id` proves a selected Studio flow.
- A standalone Python invocation proves only that module.

For a whole-app claim, require the correct startup flow, the intended browser/profile, the requested input scope, and a non-empty, structurally valid business result. Start/end logs, a short successful task, a page opening, or a file existing alone are insufficient. Mark CAPTCHA handling or manual browser intervention as assisted execution.

For date-driven jobs, separate test mode from production mode. Use an explicit timezone and calendar rule, validate the computed range, and ensure downstream imports/preflight use the same batch. Never change a historical batch's dates in place to make it appear current.

## Handle browser and data layers

Keep these states separate:

- 影刀 client login and local API session;
- Studio edit lock and unsaved state;
- Chrome/Profile and target site login;
- page identity, selected shop/account, and permissions;
- download completion and file identity;
- workbook schema, row counts, amounts, and dependent manifests;
- notifications accepted by an API versus delivered/read by a recipient.

After switching a shop or account, reread the page identity and stable backend identifier before exporting. For downloads, prove the current batch file by path, timestamp/ownership where available, and SHA-256; do not accept an old same-named file. For JSON manifests, update paths and dependent hashes in topological order. Preserve binary workbook/document/image bytes unless the requested business transformation explicitly changes them.

## Deliver and report

For delivery, separate source code from runtime materials when the user requests it. Include configuration, private credential paths, output data, logs, acceptance reports, and instructions only when needed by the runtime. Keep old credentials out of the destination and never echo them. Retain a rollback backup when moving or rewriting files.

Report in this order:

1. concrete outcome;
2. exact app/flow/files and call chain;
3. evidence and validation;
4. limitations, unverified layers, and next action.

Use `references/reporting-and-boundaries.md` for the required distinctions. Finish a terminal task with a lightweight learning review. Only write a reusable skill rule when the evidence is reproducible, generalizable, and the user has authorized skill maintenance.

## Additional resources

- `references/cli-mcp-and-runtime.md` — official CLI surface, local MCP schema discovery, runtime/version boundaries, and community API tradeoffs.
- `references/app-and-codeflow.md` — app discovery, startup-flow tracing, CodeFlow/visual-block editing, save/compile, and publication boundaries.
- `references/browser-data-evidence.md` — Profile/page identity, selectors, switching, downloads, workbook contracts, hashes, and notification evidence.
- `references/migration-and-credentials.md` — safe runtime-file migration, private credentials, rollback, and path/hash dependency handling.
- `references/reporting-and-boundaries.md` — report format, evidence levels, quota, assisted runs, and forbidden inferences.

Scripts are intentionally read-only or offline:

- `scripts/operator_probe.py` — discover the local CLI, inspect help/contracts, and optionally read live health/state/auth without running business work.
- `scripts/validate_skill.py` — validate frontmatter, links, script syntax, and installed-copy parity.
- `scripts/test_operator_tools.py` — offline regression checks for the probe and quota parser.
