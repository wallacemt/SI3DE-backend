from flask import Blueprint, request, jsonify
from datetime import datetime
from db.database import users_collection
from config.auth import hash_password, verify_password
from utils.jwtUtils import create_jwt_token

auth_bp = Blueprint("auth", __name__)

INSTITUTION_DOMAIN = "@aluno.uniruy.edu.br"

@auth_bp.route("/auth/login", methods=["POST"])
def login():
    data = request.json
    email = data.get("email")
    password = data.get("password")

    if not email or not password:
        return jsonify({"error": "Email e senha são obrigatórios"}), 400

    if not email.endswith("uniruy.edu.br"):
        return jsonify({"error": "Email fora do domínio institucional"}), 403

    user = users_collection.find_one({"email": email})

    if user:
        if not verify_password(password, user["password"]):
            return jsonify({"error": "Senha incorreta"}), 401
        
        users_collection.update_one(
            {"_id": user["_id"]},
            {"$set": {"acessAt": datetime.utcnow()}}
        )

        token = create_jwt_token(user["_id"], user["email"], user["role"])

        return jsonify({
            "nome": user["nome"],
            "email": user["email"],
            "role": user["role"],
            "isFullProfile":user[ "isFullProfile"],
            "jwtToken": token,
            "acessAt": datetime.utcnow()
        }), 200
    else:
        nome = email.split("@")[0] 
        role = email.endswith("professor.uniruy.edu.br") and "teacher" or "student"
        new_user = {
            "nome": nome,
            "email": email,
            "password": hash_password(password),
            "role": role, 
            "acessAt": datetime.utcnow(),
            "isFullProfile": False
        }

        result = users_collection.insert_one(new_user)
        token = create_jwt_token(result.inserted_id, email, role)
        return jsonify({
            "nome": nome,
            "email": email,
            "role": role,
            "jwtToken": token,
            "acessAt": new_user["acessAt"],
            "isFullProfile": new_user.get("isFullProfile", False)
        }), 201


