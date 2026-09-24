# App and CodeFlow procedure

## Discover

Resolve the app by ID and type, inspect the current editing session, then read the startup setting and every flow on the path to the target behavior. For CodeFlow, read the complete source. For visual flows, list blocks with pagination and inspect forms for real prototype names and fields. Read parameters and globals only after filtering secrets.

Trace:

`app startup → visual/CodeFlow entry → process.run/module import → browser/Profile → page identity → download/API → transformation → manifest/output → notification`.

Do not treat a named `main`, a metadata startup ID, or a short successful run as proof that the intended path executes. Look for the actual browser or file side effect.

## Edit

Use exact unique replacements for CodeFlow source. For visual blocks, insert a known prototype, read its form, fill only fields from that form, and read back the structure. Never invent a prototype name or input schema from display text.

For selector work, distinguish a temporary exploration reference from a saved application selector. After capture, read the selector library and run the smallest authorized check that uses the application copy.

## Save and verify

Run `studio app save`, then `studio diagnostics snapshot`. Read the flow again and confirm `has_unsaved_changes=false`. Close/synchronize only when required. Publishing, cloud synchronization, and another computer's installed copy require separate evidence.

## Whole-app execution

Use `console task run --app-id` for an application claim. Record the real task ID and inspect status/logs with the same ID. Validate the target Profile, browser page, input date range, output manifest, expected headers, non-empty rows where applicable, and file hashes. An assisted CAPTCHA or manually changed page must be reported as assisted.
