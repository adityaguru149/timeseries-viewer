from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routes import router


def get_application() -> FastAPI:
    app = FastAPI(title="REST server")
    app.add_middleware(
        CORSMiddleware,
        allow_origins=['*'],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    app.include_router(
        router,
        prefix="/meter",
        tags=["meter"],
        responses={404: {"description": "Not found"}},
    )
    return app
