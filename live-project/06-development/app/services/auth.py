import bcrypt
from sqlalchemy.orm import Session

from app.config import Settings
from app.models.ops_user import OpsUser


def hash_password(password: str) -> str:
    return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")


def verify_password(password: str, password_hash: str) -> bool:
    return bcrypt.checkpw(password.encode("utf-8"), password_hash.encode("utf-8"))


def ensure_ops_user(db: Session, settings: Settings) -> None:
    existing = db.query(OpsUser).filter(OpsUser.username == settings.ops_username).first()
    if existing is not None:
        return
    user = OpsUser(
        username=settings.ops_username,
        password_hash=hash_password(settings.ops_password),
    )
    db.add(user)
    db.commit()


def authenticate_ops(db: Session, username: str, password: str) -> bool:
    user = db.query(OpsUser).filter(OpsUser.username == username).first()
    if user is None:
        return False
    return verify_password(password, user.password_hash)
