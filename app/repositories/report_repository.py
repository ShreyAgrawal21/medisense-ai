from sqlalchemy.orm import Session # pyright: ignore[reportMissingImports]

from app.models.report import Report


class ReportRepository:

    def __init__(self, db: Session):
        self.db = db

    def create(self, report: Report) -> Report:
        """
        Save report metadata to database.
        """

        self.db.add(report)
        self.db.commit()
        self.db.refresh(report)

        return report

    def get_by_id(self, report_id: int) -> Report | None:
        """
        Get report by ID.
        """

        return (
            self.db.query(Report)
            .filter(Report.id == report_id)
            .first()
        )

    def get_user_reports(self, user_id: int):
        """
        Get all reports uploaded by a user.
        """

        return (
            self.db.query(Report)
            .filter(Report.user_id == user_id)
            .order_by(Report.uploaded_at.desc())
            .all()
        )