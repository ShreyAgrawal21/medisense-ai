from sqlalchemy.orm import Session # pyright: ignore[reportMissingImports]

from app.models.user import User
from app.repositories.user_repository import UserRepository
from app.schemas.user import UserCreate
from app.core.exceptions import UserAlreadyExistsException


class UserService:
    """Business logic for users."""

    def __init__(self, db: Session):
        self.repository = UserRepository(db)

    def register_user(self, data: UserCreate) -> User:

        existing = self.repository.get_by_email(data.email)

        if existing:
            raise UserAlreadyExistsException()

        user = User(
            full_name=data.full_name,
            email=data.email,
            hashed_password=data.password,
        )

        return self.repository.create(user)