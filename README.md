# Template for python repositories.
[![Lint](https://github.com/axioma-ai-labs/python-template/actions/workflows/ci-lint.yml/badge.svg)](https://github.com/axioma-ai-labs/python-template/actions/workflows/ci-lint.yml)

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Development](#development)

## Overview

This project is a template for Python repositories. It includes a Makefile with commands for 
formatting, linting, and installing dependencies. It also includes a pre-configured Github Actions 
workflow for CI/CD.

Let the following note be in your project-specific Readme file:

> [!NOTE]
> This project uses the [python-template](https://github.com/axioma-ai-labs/python-template)

## Features

### 1. Pyenv and Pipenv

The project uses Pyenv for managing Python versions and Pipenv for managing dependencies. Find more
details in the [Development](#development) section.

### 2. Pydantic

The project uses `Pydantic` for data validation and settings management.

### 3. Ruff, Isort, Mypy

The project uses `Ruff` for formatting, `Isort` for sorting imports, and `Mypy` for static typing. 
Recommended to use with `Makefile` commands. For more information look at the 
[Makefile](./Makefile).

### 4. Github Actions

The project uses Github Actions for CI/CD. Look at the [.github/workflows](.github/workflows) for 
more information. The package includes the linting workflow per default.

### 5. Makefile

The project uses Makefile for automating tasks. Look at the [Makefile](./Makefile) for more 
information.

The provided Makefile includes the following commands:

```
make deps    # Install dependencies
make format  # Format code
make lint    # Lint code
```

## Development

### Pyenv and Pipenv

#### Overview

You will need to have Python 3.12 and pipenv installed. The next step is to checkout the repository 
and install the Python dependencies. Then, you will be able to utilize the CLI and run the tests. 
The following assumes a Debian/Ubuntu machine; your mileage may vary.

#### Prerequisites

You can use pyenv for getting a specific python version. Once you have pyenv installed, you can 
install a specific python version:

```
pyenv install 3.12
```

Install pipenv:

```
pip install --user pipenv
```

#### Install Dependencies

You can use the provided Makefile files to install the dependencies.

```
make deps
```

Alternatively, you can install the dependencies manually:

```
pipenv install --dev
```

#### Setup Environment Variables

You can use the provided `.env.example` file to setup the environment variables. 

```
cp .env.example .env
```
