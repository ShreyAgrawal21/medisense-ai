import importlib

from sqlalchemy.orm import DeclarativeBase # pyright: ignore[reportMissingImports]


class Base(DeclarativeBase):
    pass


# Import the models module so SQLAlchemy registers all model classes.
# Avoid wildcard import which can cause undefined-name detection issues.
importlib.import_module("app.models")  # pragma: no cover