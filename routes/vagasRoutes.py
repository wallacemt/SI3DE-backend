from flask import Blueprint, request, jsonify
from middlewares.authRequired import auth_required
from db.database import vagas_collection
from fastapi.encoders import jsonable_encoder
from pymongo import ASCENDING, DESCENDING
import re

vagas_bp = Blueprint("vagas", __name__)

@vagas_bp.route('/vagas', methods=['GET'])
@auth_required(["student", "teacher"])
def get_vagas():
    try:
        page = int(request.args.get('page', 1))
        limit = int(request.args.get('limit', 10))
    except ValueError:
        return jsonify({"error": "Parâmetros 'page' e 'limit' devem ser inteiros."}), 400

    skip = (page - 1) * limit

    search = request.args.get('search', "").strip()
    modalidade = request.args.get('modalidade')
    nivel = request.args.get('nível')
    empresa = request.args.get('empresa')
    plataforma = request.args.get('plataforma')
    turno = request.args.get('turno')

    query = {}

    if search:
        import re
        regex = re.compile(re.escape(search), re.IGNORECASE)
        query["$or"] = [
            {"title": regex},
            {"description": regex},
            {"empresa": regex},
            {"requisitos": regex},
            {"turno": regex}
        ]

    if modalidade:
        query["modalidade"] = modalidade.lower()
    if nivel:
        query["nível"] = nivel.lower()
    if empresa:
        query["empresa"] = empresa
    if plataforma:
        query["publicationPlataform"] = plataforma
    if turno:
        query["turno"] = turno.lower()

    vagas_cursor = vagas_collection.find(query).skip(skip).limit(limit).sort("createdAt", -1)
    total = vagas_collection.count_documents(query)

    # Função de serialização
    def serialize_vaga(vaga):
        vaga["_id"] = str(vaga["_id"])
        return vaga

    vagas = [serialize_vaga(vaga) for vaga in vagas_cursor]

    return jsonify({
        "vagas": vagas,
        "page": page,
        "limit": limit,
        "total": total,
        "pages": (total + limit - 1) // limit
    }), 200
