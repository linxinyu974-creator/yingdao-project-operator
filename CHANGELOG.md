# Changelog

## 0.4.0 - 2026-09-09

- Add startup-flow preflight and distinguish whole-app runs from Studio flow and single CodeFlow runs.
- Detect successful no-op runs caused by empty entry flows, editing locks, or missing expected side effects.

## 0.3.0 - 2026-09-08

- Add the standalone `structured-thinking-toolkit` skill with targeted methods for clarification, research, verification, decision experiments and explicit self-reflection.
- Keep the structured-thinking references isolated from the Yingdao operator skill so each can be installed and invoked independently.

## 0.2.0 - 2026-09-07

- Add task routing for CodeFlow, visual flows, selectors, Profiles, databases, files and notifications.
- Add executable call-chain tracing rules and stop conditions for ambiguous targets.
- Distinguish CLI discovery/run/log capabilities from application-internal editing.
- Add shop navigation modes: `profile`, `in-page`, `api` and `direct-url`.
- Add selector/debugging guidance based on official Yingdao documentation.
- Add evidence-report template, research sources and repository hygiene rules.

## 0.1.0 - 2026-09-07

- Initial ShadowBot operator skill and references.
