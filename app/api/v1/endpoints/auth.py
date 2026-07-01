from fastapi import APIRouter, Depends # pyright: ignore[reportMissingImports]
from sqlalchemy.orm import Session # pyright: ignore[reportMissingImports]

from app.database.dependencies import get_db
from app.schemas.token import Token
from app.schemas.user import UserLogin
from app.services.user_service import UserService

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"],
)


@router.post(
    "/login",
    response_model=Token,
)
def login(
    credentials: UserLogin,
    db: Session = Depends(get_db),
):
    service = UserService(db)

    access_token = service.login_user(
        credentials.email,
        credentials.password,
    )

    return {
        "access_token": access_token,
        "token_type": "bearer",
    }