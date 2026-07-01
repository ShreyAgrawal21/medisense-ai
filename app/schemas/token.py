from pydantic import BaseModel # pyright: ignore[reportMissingImports]


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: str | None = None