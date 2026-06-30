from fastapi import APIRouter # pyright: ignore[reportMissingImports]

router = APIRouter()


@router.get("/health", tags=["Health"])
def health_check():
    return {
        "status": "healthy",
        "service": "MediSense AI"
    }


@router.get("/db-test", tags=["Health"])
def db_test():
    from sqlalchemy import text # pyright: ignore[reportMissingImports]
    from app.database.session import engine

    with engine.connect() as connection:
        connection.execute(text("SELECT 1"))

    return {
        "database": "Connected Successfully"
    }