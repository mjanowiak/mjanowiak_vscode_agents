---
description: High-level repository structure and purpose guidance for Copilot.
applyTo: '*'
---

Repository tree
---------------
This section is generated from the live repository layout. Refresh it with `python scripts/update_repo_tree.py`.

Install (macOS/Homebrew):

```bash
brew install tree
```

The updater script uses this command and ignores `.git`, `node_modules`, `.venv`, and `__pycache__`:

```bash
tree -a -I '.git|node_modules|.venv|__pycache__' -L 3
```

<!-- repo-tree:start -->
```text
.
├── .github
│   └── instructions
│       └── copilot.instructions.md
├── .gitignore
├── .python-version
├── README.md
├── assets
│   └── .keep
├── data
│   └── .keep
├── dependencies
│   └── .keep
├── docs
│   └── .keep
├── main.py
├── notebooks
│   └── .keep
├── pyproject.toml
├── scripts
│   └── update_repo_tree.py
├── src
│   └── .keep
├── tests
│   └── .keep
└── uv.lock

11 directories, 15 files
```
<!-- repo-tree:end -->


Guidance for the agent
----------------------
- When asked to add or modify code, place library code in `src/` and tests in `tests/`.
- Put reusable test data in `data/` and avoid committing large binary files; use pointers or `.gitignore` as needed.
- Store images or docs assets in `assets/` and reference them with relative paths.
- Keep notebooks focused on examples and exploration; avoid placing production code inside notebooks.

If unsure where to put a new file
--------------------------------
Ask whether the file is library code, a test, sample data, documentation asset, or an exploratory notebook. Suggest the appropriate location from the list above.
