from pydantic import BaseModel, EmailStr, ConfigDict # pyright: ignore[reportMissingImports]


class UserBase(BaseModel):
    full_name: str
    email: EmailStr


class UserCreate(UserBase):
    password: str


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class UserResponse(BaseModel):
    id: int
    full_name: str
    email: EmailStr

    model_config = ConfigDict(
        from_attributes=True
    )