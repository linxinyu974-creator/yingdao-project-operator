# CLI, MCP, runtime, and source comparison

## Official baseline

The official public repository is [ying-dao/skills](https://github.com/ying-dao/skills). Its current tree exposes `shadowbot-cli`, with English, Chinese, macOS, and 信创 variants. The CLI skill establishes the useful baseline: execute real commands only, discover non-fast paths with help, check the session first, quote Windows paths, preserve user-provided values, and surface exact JSON errors.

Use the local executable and current help as the authority for command names and flags. Do not copy a path from a README. In this Windows environment, Studio commands require `SWITCH_STUDIO_MCP_CLI_SUPPORT=1`.

## Local MCP compatibility

When a wrapper reports a schema error for an argument absent from help, discover the current local endpoint from the temporary CLI port file and inspect only the needed `tools/list` entries. The endpoint and tool names are version-specific. Check JSON-RPC errors, MCP `isError`, and business `success`; HTTP 200 alone is not success.

Keep CLI session, Studio run, console task, and MCP request IDs distinct. A CLI timeout does not stop a task. Observe the original task before considering any retry.

## Community material adopted selectively

- [HnBigVolibear/yingdao_robot_run_api_manage_and_skill](https://github.com/HnBigVolibear/yingdao_robot_run_api_manage_and_skill) contributes useful local robot listing/status concepts. Do not copy its automatic user-directory selection, persistent `setx`, or global hotkey stop behavior without explicit review.
- [1zsleep/shadowbot-skill](https://github.com/1zsleep/shadowbot-skill) contributes useful visual-block clipboard and instruction-schema ideas. Treat its migration and credential-database details as optional, version-specific material.
- [cicbyte/xbot-api-skill](https://github.com/cicbyte/xbot-api-skill) is useful as an XBot API index. Verify each SDK method in the installed runtime; its examples are not proof of the current application contract.
- [logorz/yingdao-rpa-skill](https://github.com/logorz/yingdao-rpa-skill) targets enterprise open APIs and access keys. Use only when the user has authorized that deployment surface and supplied the required credentials.

Do not automatically combine community skills. Different repositories target Hermes, OpenClaw, enterprise APIs, or a particular installation layout.

## Runtime boundary

The local app may use an embedded Python interpreter that differs from system Python. Validate dependencies with the app's Studio/runtime evidence. `py_compile`, imports in a system interpreter, metadata read-back, and a saved editor state are local checks; they do not prove a whole-app business run or publication to another computer.
