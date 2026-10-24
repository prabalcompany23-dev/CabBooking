from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from starlette.middleware.sessions import SessionMiddleware

from app import db as db_module
from app.config import get_settings
from app.routers import ops, player
from app.services.auth import ensure_ops_user


@asynccontextmanager
async def lifespan(app: FastAPI):
    settings = get_settings()
    db = db_module.SessionLocal()
    try:
        ensure_ops_user(db, settings)
    finally:
        db.close()
    yield


app = FastAPI(title="Book-a-Ride R1", lifespan=lifespan)
settings = get_settings()

app.add_middleware(SessionMiddleware, secret_key=settings.secret_key)
app.mount("/static", StaticFiles(directory="app/static"), name="static")

app.include_router(player.router)
app.include_router(ops.router)


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}
