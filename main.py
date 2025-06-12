from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from loguru import logger
import time
from src.services import user, uploades

app = FastAPI(title="Lost and Found User Management")

app.include_router(user.router, prefix="/users", tags=["users"])
app.include_router(uploades.router, prefix="/images", tags=["images"])

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.middleware("http")
async def log_requests(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    logger.info(f"{request.method} {request.url} - {response.status_code} in {process_time:.2f}s")
    return response