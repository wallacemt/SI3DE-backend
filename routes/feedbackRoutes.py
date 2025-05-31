from bson.errors import InvalidId
from flask import Blueprint, request, jsonify, g
from datetime import datetime
from middlewares.authRequired import auth_required
from db.database import feedback_collection, users_collection, profiles_collection
from bson import ObjectId

feedback_bp = Blueprint("feedback", __name__)


@feedback_bp.route('/feedback/new', methods=['POST'])
@auth_required(["student"])
def post_feedback():
    data = request.get_json()

    tipo = data.get("tipo")
    mensagem = data.get("mensagem")

    if not tipo or not mensagem:
        return jsonify({"error": "Campos 'tipo' e 'mensagem' são obrigatórios."}), 400

    feedback = {
        "user_id": g.current_user_id,
        "tipo": tipo.strip().lower(),
        "mensagem": mensagem.strip(),
        "createdAt": datetime.utcnow()
    }

    feedback_collection.insert_one(feedback)

    return jsonify({"message": "Feedback enviado com sucesso!"}), 201


@feedback_bp.route('/feedback', methods=['GET'])
@auth_required(["teacher"])
def get_feedbacks():
    feedback_docs = list(feedback_collection.find().sort("createdAt", -1))
    response = []

    for fb in feedback_docs:
        user_id = fb["user_id"] if isinstance(fb["user_id"], ObjectId) else ObjectId(fb["user_id"])
        user = users_collection.find_one({"_id": user_id})
        profile = profiles_collection.find_one({"user_id": str(user_id)})
        curso = ""
        if profile:
            curso_raw = profile.get("curso", "")
            if curso_raw:
                curso = curso_raw.replace("_", " ").capitalize()

        feedback_dict = {
            "id": str(fb["_id"]),
            "tipo": fb.get("tipo", ""),
            "mensagem": fb.get("mensagem", ""),
            "createdAt": fb.get("createdAt").isoformat() if fb.get("createdAt") else None,
            "nome": user["nome"] if user else "",
            "email": user["email"] if user else "",
            "curso": curso,
        }

        response.append(feedback_dict)

    return jsonify({"feedbacks": response}), 200


@feedback_bp.route('/feedback/<feedback_id>', methods=['DELETE'])
@auth_required(["teacher"])
def delete_feedback(feedback_id):
    try:
        _id = ObjectId(feedback_id)
    except InvalidId:
        return jsonify({"error": "ID inválido"}), 400

    result = feedback_collection.delete_one({"_id": _id})
    if result.deleted_count == 0:
        return jsonify({"error": "Feedback não encontrado"}), 404

    return jsonify({"message": "Feedback deletado com sucesso."}), 200
