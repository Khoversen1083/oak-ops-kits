---
name: agent-browser
description: Browser automation for AI agents via the agent-browser CLI (Chrome/CDP, no Playwright). Use when the user asks to open a webpage, click, fill a form, log in to a site, extract data, take a screenshot, test a web app, or automate any browser flow. Replaces the playwright-cli skill.
allowed-tools: Bash(agent-browser:*)
---

# agent-browser

Load the current usage guide on demand:

```bash
agent-browser skills get core
```

Read the output before running any agent-browser commands. The stub stays in
sync with the installed CLI version (currently produced by `agent-browser`
binary at `/opt/homebrew/bin/agent-browser`).

For specialized workflows, list available sub-skills:

```bash
agent-browser skills list
```
