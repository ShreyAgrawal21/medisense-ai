import os  # noqa: F401
import uuid
from pathlib import Path

from fastapi import HTTPException, UploadFile # pyright: ignore[reportMissingImports]

# Allowed extensions
ALLOWED_EXTENSIONS = {
    "pdf",
    "png",
    "jpg",
    "jpeg",
}

# Maximum file size (20 MB)
MAX_FILE_SIZE = 20 * 1024 * 1024

# Upload folder
UPLOAD_DIR = Path("uploads")
UPLOAD_DIR.mkdir(exist_ok=True)


def validate_file(file: UploadFile):
    """
    Validate file extension.
    """

    extension = file.filename.split(".")[-1].lower()

    if extension not in ALLOWED_EXTENSIONS:
        raise HTTPException(
            status_code=400,
            detail="Unsupported file type.",
        )


async def save_upload_file(file: UploadFile):
    """
    Save uploaded file with UUID filename.
    """

    extension = file.filename.split(".")[-1].lower()

    unique_filename = f"{uuid.uuid4()}.{extension}"

    file_path = UPLOAD_DIR / unique_filename

    content = await file.read()

    if len(content) > MAX_FILE_SIZE:
        raise HTTPException(
            status_code=400,
            detail="File size exceeds 20 MB.",
        )

    with open(file_path, "wb") as buffer:
        buffer.write(content)

    return {
        "stored_filename": unique_filename,
        "original_filename": file.filename,
        "file_size": len(content),
        "file_type": extension,
        "file_path": str(file_path),
    }