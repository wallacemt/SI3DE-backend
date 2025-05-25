from flask import Blueprint, jsonify, g
from middlewares.authRequired import auth_required
from db.database import users_collection, profiles_collection

faculty_bp = Blueprint("faculty", __name__)


@faculty_bp.route('/faculty/students', methods=['GET'])
@auth_required(["teacher"])
def get_students():
    students = []
    for user in users_collection.find({"role": "student", "isFullProfile": True}):
        user["_id"] = str(user["_id"])
        profile = profiles_collection.find_one({"user_id": user["_id"]})
        if profile:
            profile["_id"] = str(profile["_id"])
            profile["curso"] = profile["curso"].replace("_", " ").title()
            user["profile"] = profile
        else:
            continue
        students.append({
            "id": user["_id"],
            "nome": user["nome"],
            "email": user["email"],
            "role": user["role"],
            "acessAt": user["acessAt"],
            "isFullProfile": user.get("isFullProfile", False),
            "profile": user["profile"]
        })
    return jsonify(students), 200

