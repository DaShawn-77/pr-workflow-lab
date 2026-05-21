# AGENTS.md — PR Workflow Lab

## Project context
A FastAPI sandbox for practicing PR + AI review workflows.
Keep it small and focused — not meant to become a real product.

## Dev environment tips
- Python 3.11+, managed by uv. Run `uv sync` to install deps.
- Start dev server: uv run uvicorn app:app --reload
- Add a dep: uv add <package>
- Do not switch to poetry/pipenv/pip — uv is intentional.

## Testing instructions
- Run all tests: uv run pytest -v
- Run with coverage: uv run pytest --cov=app --cov-report=term-missing
- Every endpoint must have: normal case + edge case + error case
- Coverage must not drop below 80 percent
- Always consider edge cases: 0, negative, very large, type mismatch

## Code style
- Full type hints on every function signature
- All endpoints return result on success, error on failure, consistent shape
- Use FastAPI Query params for validation
- Docstrings on public functions

## PR instructions
- Title format: [scope] imperative summary  (e.g. [api] Add power endpoint)
- Run uv run pytest before committing
- Reference issue with Closes #N in PR description
- New endpoint must include its test in the same PR

## Out of scope (do not auto-modify)
- .github/workflows/ — needs explicit human approval
- pyproject.toml Python version constraint
- AGENTS.md itself — propose changes via PR with rationale
