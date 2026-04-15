from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from src.core.config import settings
from src.api.routes import router

app = FastAPI(
    title=settings.app_name,
    version="1.0.0"
)

app.include_router(router)

@app.exception_handler(ValueError)
async def value_error_handler(request: Request, exc: ValueError):
    return JSONResponse(
        status_code=400,
        content={
            "error": "bad request",
            "detail": str(exc)
        }
    )

@app.exception_handler(NotImplementedError)
async def not_implemented_handler(request: Request, exc: NotImplementedError):
    return JSONResponse(
        status_code=501,
        content={
            "error": "not_implemented",
            "detail": str(exc)
        }
    )

@app.exception_handler(Exception)
async def generic_error_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=500,
        content={
            "error": "internal_server_error",
            "detail": "An unexpected error occurred"
        }
    )

@app.get("/health")
def health_check():
    return {
        "status": "ok",
        "environment": settings.environment,
        "llm_provider": settings.llm_provider
    }