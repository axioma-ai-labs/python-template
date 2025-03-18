from enum import Enum


class Environment(Enum):
    DEVELOPMENT = "development"
    PRODUCTION = "production"
    CI = "ci"
