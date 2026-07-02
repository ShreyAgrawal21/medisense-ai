from datetime import datetime

from sqlalchemy import ( # pyright: ignore[reportMissingImports]
    Column,
    DateTime,
    ForeignKey,
    Integer,
    String,
)

from app.database.base import Base

from sqlalchemy import Text # pyright: ignore[reportMissingImports]


class Report(Base):
    __tablename__ = "reports"

    id = Column(Integer, primary_key=True, index=True)

    user_id = Column(
        Integer,
        ForeignKey("users.id"),
        nullable=False,
    )

    original_filename = Column(
        String(255),
        nullable=False,
    )

    stored_filename = Column(
        String(255),
        nullable=False,
        unique=True,
    )

    file_type = Column(
        String(50),
        nullable=False,
    )

    file_size = Column(
        Integer,
        nullable=False,
    )

    status = Column(
        String(50),
        default="uploaded",
    )

    uploaded_at = Column(
        DateTime,
        default=datetime.utcnow,
    )
    
    extracted_text = Column(Text, nullable=True)