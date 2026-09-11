# Changelog

## 1.1.0 - 2026-09-11

- Add a mandatory, terminal-state learning review for every Yingdao skill invocation.
- Separate evidence-backed reusable candidates from project notes and from authorized skill edits.
- Define rules that prevent credentials, CAPTCHA data, transient selectors, and unverified hypotheses from becoming skill knowledge.

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
## 0.4.1

- 增加个人版/社区版 CLI 每日运行额度耗尽的识别、停止重试和恢复规则。
- 增加跨运行下载文件识别、同名旧文件和文件占用的校验要求。
- 增加页面首次使用引导弹窗在业务页进入后的清理时机。
# 1.0.0 - 2026-09-10

- Reframe the project from a project-specific troubleshooting collection into an executable ShadowBot operations manual.
- Add environment/state, runtime, maintenance, and read-only operator probe guidance.
- Separate platform rules, user architecture choices, temporary diagnosis, and business E2E evidence.
