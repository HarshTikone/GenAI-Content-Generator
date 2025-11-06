from flask import request, jsonify, Blueprint, current_app
from .models import User
from . import db
from .utils import hash_password, verify_password, create_jwt, decode_jwt
from functools import wraps

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/register", methods=["POST"])
def register():
    data = request.get_json() or {}
    email = data.get("email")
    password = data.get("password")
    name = data.get("name", "")
    if not email or not password:
        return jsonify({"error": "email and password required"}), 400
    if User.query.filter_by(email=email).first():
        return jsonify({"error": "user already exists"}), 400
    user = User(email=email, password_hash=hash_password(password), name=name)
    db.session.add(user)
    db.session.commit()
    token = create_jwt({"user_id": user.id, "email": user.email})
    return jsonify({"token": token, "user": {"id": user.id, "email": user.email, "name": user.name}}), 201

@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.get_json() or {}
    email = data.get("email")
    password = data.get("password")
    if not email or not password:
        return jsonify({"error": "email and password required"}), 400
    user = User.query.filter_by(email=email).first()
    if not user or not verify_password(password, user.password_hash):
        return jsonify({"error": "invalid credentials"}), 401
    token = create_jwt({"user_id": user.id, "email": user.email})
    return jsonify({"token": token, "user": {"id": user.id, "email": user.email, "name": user.name}}), 200

def auth_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth_header = request.headers.get("Authorization", "")
        if not auth_header.startswith("Bearer "):
            return jsonify({"error": "authorization required"}), 401
        token = auth_header.split(" ", 1)[1].strip()
        try:
            payload = decode_jwt(token)
        except Exception as e:
            return jsonify({"error": "invalid token", "message": str(e)}), 401
        request.user = payload
        return f(*args, **kwargs)
    return decorated
