import os


class Config:
    """Base configuration class."""

    SQLALCHEMY_DATABASE_URI = os.getenv(
        "DATABASE_URL", "sqlite:///hrms.db"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
