# Cloud Mode

## What is Cloud Mode?

**Cloud mode** refers to running your VS Code environment and GitHub Copilot agent sessions in the cloud rather than on a local machine. It enables development workflows that do not require local compute resources.

## Common Cloud Mode Environments

### GitHub Codespaces

[GitHub Codespaces](https://github.com/features/codespaces) is a cloud-hosted development environment backed by a virtual machine. It provides:

- A full VS Code experience in a browser or via the VS Code desktop app (connected remotely).
- Pre-configured dev containers so your workspace is reproducible and consistent.
- Access to GitHub Copilot and its agents just as you would locally.

### vscode.dev / github.dev

Opening any GitHub repository with `github.dev` (replace `.com` with `.dev` in the URL) or navigating to [vscode.dev](https://vscode.dev) provides a lightweight, browser-based VS Code instance. This is useful for quick edits and code browsing, but has limited terminal / runtime support.

## Cloud Mode and GitHub Copilot Agents

When running in cloud mode (Codespaces or vscode.dev), GitHub Copilot and its coding agents work the same way as in a local VS Code installation:

- Agent instructions from `.github/instructions/` are applied automatically.
- General Copilot instructions from `.github/copilot-instructions.md` are respected.
- All agent prompts (`.prompt.md` files) and instruction files continue to guide AI behaviour.

## Why Use Cloud Mode?

| Benefit | Description |
|---------|-------------|
| **Zero local setup** | No need to install dependencies or configure your machine. |
| **Consistency** | Every team member works from the same environment definition. |
| **Accessibility** | Work from any device with a browser. |
| **Performance** | Offload compute-heavy tasks to cloud VMs. |

## Quick Start with GitHub Codespaces

1. Open this repository on GitHub.
2. Click **Code → Codespaces → Create codespace on `main`**.
3. VS Code opens in your browser with the full workspace ready.
4. GitHub Copilot agents and instructions are automatically available.

---

*See the [README](../README.md) for a general overview of this workspace.*
