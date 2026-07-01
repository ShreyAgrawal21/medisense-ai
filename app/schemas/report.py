from datetime import datetime

from pydantic import BaseModel, ConfigDict # pyright: ignore[reportMissingImports]


class ReportResponse(BaseModel):
    id: int
    original_filename: str
    stored_filename: str
    file_type: str
    file_size: int
    status: str
    uploaded_at: datetime

    model_config = ConfigDict(from_attributes=True)