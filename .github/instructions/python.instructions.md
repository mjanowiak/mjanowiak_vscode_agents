---
description: Instructions for Python Files.
applyTo: '**/*.py'
---
<!-- Tip: Use /create-instructions in chat to generate content with agent assistance -->

Purpose
-------
Provide concise, project-specific guidelines that AI should follow when generating, reviewing, or editing Python code in this repository.

Core Principles
---------------
- Keep code simple and readable; prefer clear names and small functions.
- Favor explicitness and correctness over cleverness.
- Comments should be brief and only explain "why", not "what" when code is clear.
- utilize python 3.13 as a default, but be mindful of compatibility with older versions if necessary.

Style & Formatting
-------------------
- Follow PEP 8 and idiomatic Python. Use `black` formatting (line length 88) where applicable.
- Use `isort` ordering: stdlib, third-party, local imports.
- Prefer `f"..."` for string formatting.

Docstrings & Comments
----------------------
- Use concise docstrings: one-line summary, then short details when necessary.
- Follow the Google Python docstring style (sections like Args, Returns, Raises).
- Include `Args`/`Returns`/`Raises` sections for non-trivial functions and public APIs.
- Keep inline comments short (one sentence) and sparing. Prefer explaining "why" not "what".

Example (Google style)
----------------------
def add(a: int, b: int) -> int:
	"""Add two integers.

	Args:
		a: First integer.
		b: Second integer.

	Returns:
		The sum of `a` and `b`.
	"""
	return a + b

Typing & APIs
-------------
- Use type hints for public functions and complex internal functions.
- Prefer simple, well-documented interfaces. Keep functions focused on a single responsibility.

Errors & Logging
-----------------
- Raise specific exception types; avoid bare `except:` blocks.
- Use the `logging` module for diagnostic messages, not `print()` in library code.

Best Practices
---------------
- Use context managers for resource handling.
- Avoid wildcard imports (`from module import *`).
- Write unit tests for new or changed behavior and place them under the `tests/` folder.

Security & Safety
------------------
- Do not hardcode secrets or credentials in code. Prefer environment variables or vault-style secrets.

Agent Prompts / Examples
-------------------------
- "Generate a concise Python function to do X. Keep comments brief and prefer clarity over cleverness. Add type hints and a short docstring."
- "Refactor this function to be simpler and split responsibilities; include a unit test example." 

What to Avoid
--------------
- Long, dense comments that repeat the code.
- Overly clever one-liners that sacrifice readability.

If unclear or ambiguous
-----------------------
Ask whether the guideline should apply repository-wide or only to certain modules, and whether a strict formatter/linters should be enforced.

ApplyTo
--------
This file applies to: `**/*.py`
