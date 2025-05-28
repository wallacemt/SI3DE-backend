from flask import Blueprint, request, jsonify, g
from middlewares.authRequired import auth_required
from db.database import vagas_collection

from db.database import users_collection, profiles_collection

vagas_bp = Blueprint("vagas", __name__)


@vagas_bp.route('/vagas', methods=['GET'])
@auth_required(["student", "teacher"])
def get_vagas():
    try:
        page = int(request.args.get('page', 1))
        limit = int(request.args.get('limit', 10))
    except ValueError:
        return jsonify({"error": "Parâmetros 'page' e 'limit' devem ser inteiros."}), 400

    profile = profiles_collection.find_one({"user_id": g.current_user_id})
    skip = (page - 1) * limit

    search = request.args.get('search', "").strip()
    modalidade = request.args.get('modalidade')
    nivel = request.args.get('nível')
    empresa = request.args.get('empresa')
    plataforma = request.args.get('plataforma')
    turno_param = request.args.get('turno')  # valor vindo da URL, se tiver

    query = {}

    # 🔁 Filtro de turno automático baseado no turno do aluno (apenas se não tiver filtro manual)
    if g.role == "student":
        turno_aluno = profile.get("turno")
        if not turno_param and turno_aluno:
            turnos_opostos = {
                "matutino": ["noturno", "vespertino", "integral"],
                "noturno": ["matutino", "vespertino", "integral"],
                "vespertino": ["matutino", "noturno", "integral"],
            }
            turno_oposto = turnos_opostos.get(turno_aluno.lower())
            if turno_oposto:
                query["turno"] = {"$in": turno_oposto}

    # 🔍 Filtro de busca textual
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

    # 📌 Outros filtros opcionais
    if modalidade:
        query["modalidade"] = modalidade.lower()
    if nivel:
        query["nível"] = nivel.lower()
    if empresa:
        query["empresa"] = empresa
    if plataforma:
        query["publicationPlataform"] = plataforma
    if turno_param:
        if (turno_param.lower() != turno_aluno.lower()):
            query["turno"] = turno_param.lower()

    vagas_cursor = vagas_collection.find(query).skip(skip).limit(limit).sort("createdAt", -1)
    total = vagas_collection.count_documents(query)

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
