from sqlalchemy.orm import Session # pyright: ignore[reportMissingImports]

from app.core.exceptions import UserAlreadyExistsException
from app.core.security import hash_password
from app.models.user import User
from app.repositories.user_repository import UserRepository
from app.schemas.user import UserCreate


class UserService:
    """
    Handles business logic related to users.
    """

    def __init__(self, db: Session):
        self.repository = UserRepository(db)

    def register_user(self, data: UserCreate) -> User:
        """
        Register a new user.
        """

        # Check if email already exists
        existing_user = self.repository.get_by_email(data.email)

        if existing_user:
            raise UserAlreadyExistsException()

        # Create user with hashed password
        user = User(
            full_name=data.full_name,
            email=data.email,
            hashed_password=hash_password(data.password),
        )

        # Save user to database
        return self.repository.create(user)
