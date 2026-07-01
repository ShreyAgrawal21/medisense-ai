from sqlalchemy.orm import Session # pyright: ignore[reportMissingImports]

from app.core.auth import create_access_token
from app.core.exceptions import (
    InvalidCredentialsException,
    UserAlreadyExistsException,
)
from app.core.security import (
    hash_password,
    verify_password,
)
from app.models.user import User
from app.repositories.user_repository import UserRepository
from app.schemas.user import UserCreate


class UserService:

    def __init__(self, db: Session):
        self.repository = UserRepository(db)

    def register_user(self, data: UserCreate) -> User:

        existing = self.repository.get_by_email(data.email)

        if existing:
            raise UserAlreadyExistsException()

        user = User(
            full_name=data.full_name,
            email=data.email,
            hashed_password=hash_password(data.password),
        )

        return self.repository.create(user)

    def login_user(
        self,
        email: str,
        password: str,
    ) -> str:

        user = self.repository.get_by_email(email)

        if not user:
            raise InvalidCredentialsException()

        if not verify_password(
            password,
            user.hashed_password,
        ):
            raise InvalidCredentialsException()

        token = create_access_token(
            {
                "sub": user.email,
            }
        )

        return token
    # Save user to database
        return self.repository.create(user)