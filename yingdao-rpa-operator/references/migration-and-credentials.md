# Migration and credentials

Separate source delivery from runtime delivery when requested. Runtime delivery may include configuration, private credential files, outputs, logs, acceptance records, and instructions. Do not copy development caches, temporary Office lock files, browser cookies, or source code unless explicitly requested.

Before rewriting paths, inventory absolute references in JSON, CSV, Markdown, and configuration. Copy binaries byte-for-byte. Back up the selected source files. Rewrite paths using a longest-match mapping, then recompute only hashes whose referenced bytes or JSON representation changed. Detect circular manifest dependencies and keep a migration manifest with old/new paths and hashes.

Credentials belong in a private file or approved secret store. Keep only its path in ordinary configuration. Do not print passwords, tokens, cookies, or full account credentials in logs, reports, test fixtures, or skill files. When replacing a credential, remove the old value from the delivered runtime tree and verify by a byte/string scan without displaying the new secret.

Do not claim migration success from file existence alone. Validate referenced files, hash chains, binary equality, configuration semantics, and the actual loaded Studio/app copy. A rollback backup is required before destructive replacement.
