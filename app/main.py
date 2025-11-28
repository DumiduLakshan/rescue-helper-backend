from fastapi import FastAPI

from app.routes import health
from app.utils.exception_handlers import register_exception_handlers
from app.utils.logging_setup import configure_logging


def create_app() -> FastAPI:
    configure_logging()
    app = FastAPI(title="Rescue API", version="0.1.0")
    register_exception_handlers(app)
    app.include_router(health.router, prefix="/api")
    return app


app = create_app()




