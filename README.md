# Apeex Framework

A modular, interface-driven web framework inspired by **Symfony**, built on top of **FastAPI**.

## 🧩 Structure
    apeex/ # Core framework (Kernel, Container, HTTP)
    adapters/ # Integrations and bridges
    bundles/ # Feature modules
    scripts/ # CLI and dev utilities
    tests/ # Unit and integration tests

## 🧰 Development

Run code checks:
black . && isort . && flake8 && mypy && pytest

**Создай `CONTRIBUTING.md`:**

# Contributing to Apeex

Thank you for contributing!

## Branching
- `main`: stable branch.
- `develop`: main development branch.
- Use feature branches: `feature/<name>`.

## Commits
Use **Conventional Commits**, e.g.:
- `feat: add DI container`
- `fix: resolve controller import`
- `chore: update dependencies`

## Code Style
- Format with `black` and `isort`
- Run `flake8` and `mypy` before committing.
- All comments in English.

## Tests
Run tests:
```bash
pytest -vx`
```
---

### 5. 🚦 CI/CD — GitHub Actions

Создай `.github/workflows/ci.yml`:
```yaml
name: CI

on:
  push:
    branches: [ main, develop ]
  pull_request:
    branches: [ main, develop ]

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout
        uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.11'

      - name: Install dependencies
        run: |
          pip install poetry
          poetry install

      - name: Lint & Type Check
        run: |
          poetry run black --check .
          poetry run isort --check-only .
          poetry run flake8 .
          poetry run mypy .

      - name: Run Tests
        run: |
          poetry run pytest -v