# Template for python repositories.
[![Lint](https://github.com/axioma-ai-labs/python-template/actions/workflows/ci-lint.yml/badge.svg)](https://github.com/axioma-ai-labs/python-template/actions/workflows/ci-lint.yml)
[![Docker](https://github.com/axioma-ai-labs/python-template/actions/workflows/docker-build.yml/badge.svg)](https://github.com/axioma-ai-labs/python-template/actions/workflows/docker-build.yml)

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

### 1. Pyenv and Poetry

The project uses Pyenv for managing Python versions and Poetry for managing dependencies. Find more
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

### Pyenv and Poetry

#### Overview

You will need to have Python 3.13 and Poetry installed. The next step is to checkout the repository 
and install the Python dependencies. Then, you will be able to utilize the CLI and run the tests. 
The following assumes a Debian/Ubuntu machine; your mileage may vary.

#### Prerequisites

You can use pyenv for getting a specific python version. Once you have pyenv installed, you can 
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

You can use the provided `.env.example` file to setup the environment variables. 

```
cp .env.example .env
```

### 6. Docker

The project uses Docker for building the image. Look at the [Dockerfile](./Dockerfile) for more 
information.

```
docker build -t python-template .
```

### 7. Testing

The project uses pytest for testing. Look at the [Makefile](./Makefile) for more information.

```
make test
```

### 8. CI/CD

The project uses Github Actions for CI/CD. Look at the [.github/workflows](.github/workflows) for 
more information. The package includes the linting and docker build workflows per default.
