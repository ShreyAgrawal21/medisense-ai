from fastapi import Depends, HTTPException, status # pyright: ignore[reportMissingImports]
from fastapi.security import OAuth2PasswordBearer # pyright: ignore[reportMissingImports]
from jose import JWTError, jwt # pyright: ignore[reportMissingModuleSource]
from sqlalchemy.orm import Session # pyright: ignore[reportMissingImports]

from app.core.config import settings
from app.database.dependencies import get_db
from app.models.user import User
from app.repositories.user_repository import UserRepository

oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="/api/v1/auth/login"
)


def get_current_user(
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(get_db),
) -> User:

    print("\n========== DEBUG ==========")
    print("Received Token:", token)

    try:
        payload = jwt.decode(
            token,
            settings.SECRET_KEY,
            algorithms=[settings.ALGORITHM],
        )

        print("Payload:", payload)

        email = payload.get("sub")
        print("Email:", email)

    except Exception as e:
        print("JWT Decode Error:", repr(e))
        raise HTTPException(
            status_code=401,
            detail="Could not validate credentials",
        )

    repository = UserRepository(db)

    user = repository.get_by_email(email)

    print("User Found:", user)

    if user is None:
        print("Database lookup failed!")
        raise HTTPException(
            status_code=401,
            detail="Could not validate credentials",
        )

    print("Authentication Successful!")

    return user