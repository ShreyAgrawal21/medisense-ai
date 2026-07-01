from fastapi import ( # pyright: ignore[reportMissingImports]
    APIRouter,
    Depends,
    File,
    UploadFile,
    status,
)
from sqlalchemy.orm import Session # pyright: ignore[reportMissingImports]

from app.database.dependencies import get_db
from app.core.dependencies import get_current_user
from app.models.user import User
from app.schemas.report import ReportResponse
from app.services.report_service import ReportService

router = APIRouter(
    prefix="/reports",
    tags=["Reports"],
)


@router.post(
    "/upload",
    response_model=ReportResponse,
    status_code=status.HTTP_201_CREATED,
)
async def upload_report(
    file: UploadFile = File(...),
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    service = ReportService(db)

    return await service.upload_report(
        current_user=current_user,
        file=file,
    )