from sqlalchemy.orm import Session # pyright: ignore[reportMissingImports]
from fastapi import UploadFile # pyright: ignore[reportMissingImports]

from app.models.report import Report
from app.models.user import User
from app.repositories.report_repository import ReportRepository
from app.utils.file_handler import validate_file, save_upload_file


class ReportService:

    def __init__(self, db: Session):
        self.repository = ReportRepository(db)

    async def upload_report(
        self,
        current_user: User,
        file: UploadFile,
    ) -> Report:
        """
        Upload a medical report.
        """

        # Validate extension
        validate_file(file)

        # Save file locally
        file_info = await save_upload_file(file)

        # Create Report object
        report = Report(
            user_id=current_user.id,
            original_filename=file_info["original_filename"],
            stored_filename=file_info["stored_filename"],
            file_type=file_info["file_type"],
            file_size=file_info["file_size"],
            status="uploaded",
        )

        # Save metadata
        return self.repository.create(report)