from typing import Generic, TypeVar

from pydantic import BaseModel # pyright: ignore[reportMissingImports]

T = TypeVar("T")


class APIResponse(BaseModel, Generic[T]):
    success: bool
    message: str
    data: T | None = None