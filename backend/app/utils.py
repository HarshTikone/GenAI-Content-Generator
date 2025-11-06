import os
import datetime
from passlib.hash import bcrypt
import jwt
from flask import current_app

def hash_password(password: str) -> str:
    return bcrypt.using(rounds=12).hash(password)

def verify_password(password: str, password_hash: str) -> bool:
    return bcrypt.verify(password, password_hash)

def _get_jwt_secret_and_alg():
    # try common locations / names (config, then env)
    secret = None
    alg = None
    try:
        secret = current_app.config.get("JWT_SECRET") or current_app.config.get("SECRET_KEY")
        alg = current_app.config.get("JWT_ALGORITHM")
    except RuntimeError:
        # no app context; fall back to env
        secret = os.getenv("JWT_SECRET") or os.getenv("SECRET_KEY")
        alg = os.getenv("JWT_ALGORITHM")
    if not secret:
        # dev fallback (only use for local testing; replace with secure secret for prod)
        secret = "dev-secret-please-change"
    if not alg:
        alg = "HS256"
    return secret, alg

def create_jwt(payload: dict, expires_minutes: int = 60*24) -> str:
    secret, alg = _get_jwt_secret_and_alg()
    data = payload.copy()
    data["exp"] = datetime.datetime.utcnow() + datetime.timedelta(minutes=expires_minutes)
    # PyJWT.encode returns a str in modern versions; ensure str
    token = jwt.encode(data, secret, algorithm=alg)
    if isinstance(token, bytes):
        token = token.decode("utf-8")
    return token

def decode_jwt(token: str) -> dict:
    secret, alg = _get_jwt_secret_and_alg()
    return jwt.decode(token, secret, algorithms=[alg])
