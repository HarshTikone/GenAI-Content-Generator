import os
from flask import Flask
from flask_cors import CORS
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from flask_sqlalchemy import SQLAlchemy
from .config import Config

db = SQLAlchemy()
limiter = Limiter(key_func=get_remote_address, default_limits=["200 per day", "50 per hour"])

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    CORS(app, origins=app.config.get("CORS_ORIGINS", "*"))
    db.init_app(app)
    limiter.init_app(app)

    with app.app_context():
        # import routes to register endpoints
        from .routes import api_bp
        app.register_blueprint(api_bp, url_prefix="/api")
        db.create_all()

    return app
