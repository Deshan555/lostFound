from fastapi import APIRouter, UploadFile, File, HTTPException
from typing import List
import os
import uuid
from loguru import logger

router = APIRouter()

UPLOAD_DIR = "static/uploads"
ALLOWED_EXTENSIONS = {".jpg", ".jpeg", ".png", ".gif"}

@router.post("/upload/")
async def upload_images(files: List[UploadFile] = File(...)):
    if not files:
        raise HTTPException(status_code=400, detail="No files provided")

    os.makedirs(UPLOAD_DIR, exist_ok=True)

    uploaded_urls = []
    for file in files:
        ext = os.path.splitext(file.filename)[1].lower()
        if ext not in ALLOWED_EXTENSIONS or not file.content_type.startswith("image/"):
            raise HTTPException(status_code=400, detail=f"Invalid file type: {file.filename}")

        unique_filename = f"{uuid.uuid4()}{ext}"
        file_path = os.path.join(UPLOAD_DIR, unique_filename)

        with open(file_path, "wb") as buffer:
            buffer.write(await file.read())

        uploaded_urls.append(f"/static/uploads/{unique_filename}")

    logger.info(f"Uploaded {len(files)} images")
    return {"uploaded_files": uploaded_urls}