# Template for Python repositories
[![CI](https://github.com/axioma-ai-labs/python-template/actions/workflows/main.yml/badge.svg)](https://github.com/axioma-ai-labs/python-template/actions/workflows/main.yml)
[![Docker](https://github.com/axioma-ai-labs/python-template/actions/workflows/docker-latest.yml/badge.svg)](https://github.com/axioma-ai-labs/python-template/actions/workflows/docker-latest.yml)

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Development](#development)

## Overview

This project is a template for Python repositories. It includes a Makefile with commands for
formatting, linting, and installing dependencies. It also includes pre-configured GitHub Actions
workflow for CI/CD.

You can add the following note to a project-specific README:

> [!NOTE]
> This project uses the [python-template](https://github.com/axioma-ai-labs/python-template)

## Features

### 1. Pyenv and Poetry

The project uses Pyenv for managing Python versions and Poetry for managing dependencies. Find more
details in the [Development](#development) section.

### 2. Pydantic, Loguru, and optional Sentry

The project uses `Pydantic` for data validation and settings management, `Loguru` for logging,
and optional `Sentry` initialization for error tracking and performance monitoring.

### 3. Custom application exceptions

The template includes reusable application exceptions in `src/core/exceptions/` and a top-level
entrypoint wrapper in `src/main.py` for consistent error handling.

### 4. Ruff, isort, mypy, and pytest

The project uses `Ruff` for formatting, `isort` for sorting imports, `mypy` for static typing,
and `pytest` for testing. Recommended to use with `Makefile` commands. For more information look at the
[Makefile](./Makefile).

### 5. GitHub Actions and Dependabot

The project uses GitHub Actions for CI/CD and includes Dependabot configuration for Python,
Docker, and GitHub Actions updates.

### 6. Makefile

The project uses Makefile for automating tasks. Look at the [Makefile](./Makefile) for more
information.

The provided Makefile includes the following commands:

```
make deps    # Install dependencies
make format  # Format code
make lint    # Lint code
make test    # Run tests
```

## Development

### Pyenv and Poetry

#### Overview

You will need to have Python 3.13 and Poetry installed. The next step is to checkout the repository
and install the Python dependencies. Then, you will be able to run the example entrypoint and tests.
The following assumes a Debian/Ubuntu machine; your mileage may vary.

#### Prerequisites

You can use pyenv for getting a specific Python version. Once you have pyenv installed, you can
install a specific python version:

```
pyenv install 3.13
```

Install Poetry (for Linux and MacOS):

```
curl -sSL https://install.python-poetry.org | python3 -
```

#### Install Dependencies

You can use the provided Makefile files to install the dependencies.

```
make deps
```

#### Add new dependencies

```
poetry add <package>
```

or if you want to add a dependency to the development group:

```
poetry add --group dev <package>
```

#### Setup Environment Variables

You can use the provided `.env.example` file to set up the environment variables.

```
cp .env.example .env
```

The default template variables are:

```env
ENVIRONMENT=development
SENTRY_DSN=
SENTRY_TRACES_SAMPLE_RATE=0.1
```

### 6. Docker

The project uses Docker for building the image. Look at the [Dockerfile](./Dockerfile) for more 
information.

```
docker build -t python-template .
```

### 7. Running the template

Run the example entrypoint:

```bash
make dev
```

The startup sequence configures logging, initializes Sentry when `SENTRY_DSN` is set, and then
runs the example application entrypoint.

### 8. Testing

The project uses pytest for testing. Look at the [Makefile](./Makefile) for more information.

```
make test
```

### 9. AI agent guidance

This repository includes `AGENTS.md` for coding-agent instructions. `CLAUDE.md` points to the same
content so both entry points stay in sync.

### 10. CI/CD

The project uses GitHub Actions for CI/CD. Look at the [.github/workflows](.github/workflows) for
more information. The package includes test/lint and Docker workflows by default.
