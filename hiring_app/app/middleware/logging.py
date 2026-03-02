import time
import logging
from fastapi import Request

logger = logging.getLogger("api_logger")
logging.basicConfig(level=logging.INFO)

async def logging_middleware(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    duration = time.time() - start_time
    logger.info(f"Method: {request.method} | Path: {request.url.path} | Time: {duration:.4f}s")
    return response
