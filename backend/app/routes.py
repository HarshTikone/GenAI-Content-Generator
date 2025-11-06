from flask import Blueprint, request, jsonify, current_app
from .auth import auth_bp, auth_required
from . import db
from .models import User, Project
from .generator import Generator
from .utils import create_jwt
from flask_limiter.util import get_remote_address
from flask_limiter import Limiter

api_bp = Blueprint("api", __name__)
api_bp.register_blueprint(auth_bp, url_prefix="/auth")

# local limiter for endpoints
limiter = Limiter(key_func=get_remote_address)

@api_bp.route("/profile", methods=["GET"])
@auth_required
def profile():
    user_id = request.user.get("user_id")
    user = User.query.get(user_id)
    if not user:
        return jsonify({"error": "user not found"}), 404
    return jsonify({"id": user.id, "email": user.email, "name": user.name})

@api_bp.route("/projects", methods=["GET"])
@auth_required
def list_projects():
    user_id = request.user.get("user_id")
    projects = Project.query.filter_by(user_id=user_id).order_by(Project.created_at.desc()).all()
    return jsonify([{"id": p.id, "title": p.title, "prompt": p.prompt, "output": p.output, "created_at": p.created_at.isoformat()} for p in projects])

@api_bp.route("/projects", methods=["POST"])
@auth_required
def create_project():
    data = request.get_json() or {}
    title = data.get("title", "Untitled")
    prompt = data.get("prompt", "")
    if not prompt:
        return jsonify({"error": "prompt required"}), 400
    user_id = request.user.get("user_id")
    project = Project(user_id=user_id, title=title, prompt=prompt)
    db.session.add(project)
    db.session.commit()
    return jsonify({"id": project.id, "title": project.title, "prompt": project.prompt}), 201

@api_bp.route("/generate", methods=["POST"])
@auth_required
@limiter.limit("10/minute")
def generate_text():
    data = request.get_json() or {}
    prompt = data.get("prompt", "")
    params = data.get("params", {})
    if not prompt:
        return jsonify({"error": "prompt required"}), 400

    gen = Generator.get()
    max_length = int(params.get("max_length", 200))
    temperature = float(params.get("temperature", 0.9))
    top_k = int(params.get("top_k", 40))
    n = int(params.get("num_return_sequences", 1))

    try:
        outputs = gen.generate(prompt, max_length=max_length, temperature=temperature, top_k=top_k, num_return_sequences=n)
    except Exception as e:
        current_app.logger.exception("generation failed")
        return jsonify({"error": "generation failed", "message": str(e)}), 500

    # store a project record optionally
    user_id = request.user.get("user_id")
    title = data.get("title", "Generated Content")
    project = Project(user_id=user_id, title=title, prompt=prompt, output=outputs[0])
    db.session.add(project)
    db.session.commit()

    return jsonify({"outputs": outputs, "project_id": project.id}), 200
