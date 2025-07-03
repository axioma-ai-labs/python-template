from enum import Enum


class Environment(Enum):
    DEVELOPMENT = "development"
    STAGING = "staging"
    CI = "ci"
    TEST = "test"
    PRODUCTION = "production"
