This file provides guidance to AI coding agents working with this repository.

## Project Overview

This repository is a reusable Python project template. It is intentionally small
and generic, so changes should prefer simple, composable patterns over
project-specific architecture.

The current template includes:

- Poetry for dependency management
- Pydantic Settings for configuration
- Loguru for logging
- Optional Sentry initialization
- Custom application exceptions
- pytest, Ruff, isort, and mypy
- Docker and GitHub Actions

When adapting this template for a real project, preserve the clean foundation
and add framework- or domain-specific code incrementally.

## Common Development Commands

```bash
make deps      # Install dependencies
make format    # Format code
make lint      # Run Ruff, isort, and mypy
make test      # Run tests
make ci-test   # Run tests with coverage
make dev       # Run the example entrypoint
```

## Core Principles

### Keep the template generic

- Do not introduce business-specific naming, copy, or architecture into the
  template.
- Prefer framework-agnostic utilities in `src/core/` unless the repository has
  clearly become tied to a framework.
- New defaults should be broadly useful to future projects, not tailored to one
  app.

### Favor minimal, explicit patterns

- Prefer small modules with obvious responsibilities.
- Avoid clever abstractions unless they clearly reduce repeated complexity.
- Keep startup wiring easy to trace from `src/main.py`.
- Make optional integrations truly optional by gating them with settings.

### Preserve clean layering

- `src/core/` is for reusable foundation code: config, logging, observability,
  exceptions, enums, and similar cross-cutting concerns.
- `src/main.py` is the composition root for startup wiring and top-level error
  handling.
- `tests/` should verify behavior, not implementation details.

## Configuration Conventions

- All configuration should live in `src/core/config.py`.
- Environment variables should be documented in `.env.example`.
- Copy `.env.example` to `.env` for local development; never commit secrets.
- Optional services must degrade cleanly when their config is absent.

Examples in this template:

- Sentry is disabled when `SENTRY_DSN` is empty.
- Logging configuration is environment-aware via `ENVIRONMENT`.

## Logging, Observability, and Errors

- Use `src/core/logging.py` for Loguru setup.
- Keep observability integrations minimal in the template. Add advanced routing,
  filtering, or framework-specific integrations only in downstream projects.
- Use custom exceptions from `src/core/exceptions/` for intentional app-level
  failures.
- Catch custom app exceptions at the top level in `src/main.py` or the
  framework-specific entrypoint, log them consistently, and exit or translate
  them there.

## Dependencies

- Use Poetry for all dependency changes.
- Keep runtime dependencies minimal.
- Add a dependency to the template only if it is broadly useful across many new
  projects.
- Remove stale dependencies when their integration is removed from the codebase.

## Testing and Verification

- Add or update focused tests for behavior changes.
- Prefer test-first changes for new features and bug fixes.
- After substantive edits, run:

```bash
make test
make lint
```

- If config, startup wiring, or dependency behavior changes, add tests for the
  new edge cases.

## Code Style

- Python 3.13 target.
- Line length: 100.
- Type hints are required for public function signatures.
- Keep comments focused on why, not what.
- Public modules and public classes should have useful docstrings.
- Avoid commented-out code.

## Template-Specific Change Guidelines

- If you add a new core capability, wire it through all relevant template entry
  points:
  - dependencies in `pyproject.toml`
  - environment variables in `.env.example`
  - startup/config code in `src/core/` or `src/main.py`
  - tests in `tests/`
  - docs in `README.md` if the capability affects setup or usage

- If you rename or remove a template feature, clean up:
  - stale tests
  - stale README references
  - stale environment variables
  - stale dependencies and lockfile entries

## What Not to Do

- Do not hardcode secrets or commit real credentials.
- Do not add service-specific architecture to the template without a clear need.
- Do not leave dead examples, mismatched tests, or outdated docs behind.
- Do not couple the template to a framework unless that is an intentional
  direction change for the repository.

## Keeping This File in Sync

Update this file whenever the template's development workflow, architectural
expectations, or core building blocks change.
