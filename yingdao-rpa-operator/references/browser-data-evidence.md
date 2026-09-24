# Browser and data evidence

Keep four browser states separate: client session, Chrome/Profile, target-site login, and business-page identity. A browser tab existing or a URL matching does not prove the correct account or shop.

After a shop/account switch, reread the stable backend identifier and displayed name. Reject stale identity, duplicate IDs, or a failed business response before exporting. Prefer a verified API/in-page switch when the application already uses one; direct URLs are valid only when the target identity is read back and proven.

For downloads, wait for completion, locate the file in the current batch directory, reject stale same-name files, and record SHA-256. For workbooks, validate actual sheet names, headers, dates, unique business keys, row counts, and amounts. `max_row` alone is not a data check.

When rewriting JSON manifests, update absolute paths and recompute dependent hashes in dependency order. Preserve business binary bytes. Do not alter event IDs merely because a historical notification log contains an old path; if a migration requires a derived ID change, keep an explicit old-to-new mapping and do not resend an accepted event.

Treat notification `accepted` as API acceptance, not proof of group delivery or read status. Keep `pending`/`unconfirmed` visible and avoid blind resends.

For date-driven workflows, calculate the range with the declared timezone. A rule such as “Beijing time, the seven complete calendar days before today” means `[today-7 days, today-1 day]`, including both endpoints. Check midnight and month/year/leap-day boundaries, then ensure the downstream preflight and import reference the same new batch.
