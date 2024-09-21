DIRS_PYTHON := src

.PHONY: help
help:
	@echo "Usage: make <target>"
	@echo
	@echo "Targets:"
	@echo "  help            This help (default target)"
	@echo "  deps            Install all dependencies"
	@echo "  format          Format source code"
	@echo "  lint            Run lint checks"

.PHONY: deps
deps:
	pipenv install --dev

.PHONY: format
format:	\
	format-ruff \
	format-isort

.PHONY: format-ruff
format-ruff:
	pipenv run ruff format --line-length 100 $(DIRS_PYTHON)

.PHONY: format-isort
format-isort:
	pipenv run isort --profile=black --line-length 100 $(DIRS_PYTHON)

.PHONY: lint
lint: \
	lint-ruff \
	lint-isort \
	lint-mypy

.PHONY: lint-ruff
lint-ruff:
	pipenv run ruff check --line-length 100 $(DIRS_PYTHON)

.PHONY: lint-isort
lint-isort:
	pipenv run isort --profile=black --line-length 100 --check-only --diff $(DIRS_PYTHON)

.PHONY: lint-mypy
lint-mypy:
	pipenv run mypy --check-untyped-defs $(DIRS_PYTHON)

# .PHONY: jupyternotebook
# jupyternotebook:
# 	pipenv run \
# 		jupyter notebook

# .PHONY: jupyterlab
# jupyterlab:
# 	cp src/bench/results_analysis.ipynb tmp.ipynb && \
# 	PYTHON=. pipenv run \
# 		jupyter lab \
# 			--ip=0.0.0.0 --allow-root --NotebookApp.custom_display_url=http://127.0.0.1:8888 \
# 			tmp.ipynb
