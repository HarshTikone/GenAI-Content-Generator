import os
from dotenv import load_dotenv

load_dotenv()

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.environ.get("JWT_SECRET", "change-me-in-prod")
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL", "sqlite:///" + os.path.join(BASE_DIR, "..", "data.sqlite"))
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MODEL_NAME = os.environ.get("MODEL_NAME", "EleutherAI/gpt-neo-125M")
    CORS_ORIGINS = os.environ.get("CORS_ORIGINS", "*")
    JWT_ALGORITHM = os.environ.get("JWT_ALGORITHM", "HS256")
    RATE_LIMIT = os.environ.get("RATE_LIMIT", "10 per minute")
