# Reporting and boundaries

Report the concrete outcome first, then:

1. app ID, flow ID, source/config paths, and the relevant call chain;
2. exact observations and evidence paths;
3. changed, saved, published, run, and verified states separately;
4. failures, skips, manual assistance, quota constraints, and unverified layers;
5. the next safe action.

Do not infer:

| Evidence | Do not claim |
|---|---|
| `py_compile` or AST success | Studio/runtime compatibility or business success |
| CLI health or auth success | Target website login or page identity |
| Saved Studio state | Cloud publication or another computer's update |
| A file exists | It belongs to the current batch or is complete |
| Start/end logs only | The intended app path ran |
| Historical quota or “remaining 1” | Current quota availability |
| API `accepted` notification | Group delivery or read status |
| One permission error | A platform-wide permission rule |

For a terminal task, perform a lightweight learning review. Write a reusable rule only when evidence is reproducible and generalizable, the scope is clear, and skill maintenance is authorized. Otherwise record the project fact in the task report only.
