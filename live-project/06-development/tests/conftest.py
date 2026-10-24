import os

import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

os.environ.setdefault("DATABASE_URL", "sqlite://")
os.environ.setdefault("SECRET_KEY", "test-secret-key")
os.environ.setdefault("PILOT_CITY", "Bengaluru")
os.environ.setdefault("PILOT_SPORT", "Badminton")
os.environ.setdefault("OPS_USERNAME", "ops")
os.environ.setdefault("OPS_PASSWORD", "test-ops-password")

from app.config import get_settings
from app import db as db_module
from app.db import Base, get_db
from app.main import app
from app.services.auth import ensure_ops_user

get_settings.cache_clear()


@pytest.fixture()
def client() -> TestClient:
    engine = create_engine(
        "sqlite://",
        connect_args={"check_same_thread": False},
        poolclass=StaticPool,
    )
    Base.metadata.create_all(bind=engine)
    TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

    db_module.engine = engine
    db_module.SessionLocal = TestingSessionLocal

    seed_db = TestingSessionLocal()
    try:
        ensure_ops_user(seed_db, get_settings())
    finally:
        seed_db.close()

    def override_get_db():
        session = TestingSessionLocal()
        try:
            yield session
        finally:
            session.close()

    app.dependency_overrides[get_db] = override_get_db
    with TestClient(app) as test_client:
        yield test_client
    app.dependency_overrides.clear()
    Base.metadata.drop_all(bind=engine)
