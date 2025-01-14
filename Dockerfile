# ====================
# Build Neurobro Agent
# ====================

FROM python:3.12-slim
WORKDIR /src

ENV LANG=C.UTF-8
ENV LC_ALL=C.UTF-8
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONFAULTHANDLER=1

# -----------------------
# Install system packages
# -----------------------

RUN apt-get update && apt-get install -y
  curl \
  && rm -rf /var/lib/apt/lists/*


RUN pip install pipenv

# -------------------------
# Create the logs directory
# -------------------------

RUN mkdir logs

# ---------------------
# Setup the environment
# ---------------------

COPY Pipfile .
COPY Pipfile.lock .

RUN PIPENV_VENV_IN_PROJECT=1 pipenv install --deploy

# ----------------------
# Runtime
# ----------------------

COPY . /src

COPY entrypoint.sh /src/entrypoint.sh

RUN chmod +x /src/entrypoint.sh

# Command to run the application
ENTRYPOINT ["/src/entrypoint.sh"]
