#!/usr/bin/bash

set -x
set -euo pipefail

# Run the main application
echo "Starting the main application..."
exec pipenv run python -m src.main
