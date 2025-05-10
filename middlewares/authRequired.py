from flask import request, jsonify, g
import jwt
from functools import wraps
from config.config import JWT_SECRET
from utils.jwtUtils import decode_jwt
def auth_required(allowed_roles=None):
    def decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            auth_header = request.headers.get('Authorization')
            if not auth_header or not auth_header.startswith('Bearer '):
                return jsonify({"error": "Token de autenticação ausente ou inválido"}), 401

            token = auth_header.split(" ")[1].strip()

            try:
                payload = decode_jwt(token=token)
                g.current_user_id = payload.get("sub") 
                g.email = payload.get("email")
                g.role = payload.get("role")
                if allowed_roles:

                    if g.role not in allowed_roles:
                        return jsonify({"error": "Acesso não autorizado"}), 403
            except jwt.ExpiredSignatureError:
                return jsonify({"error": "Token expirado"}), 401
            except jwt.InvalidTokenError:
                return jsonify({"error": "Token inválido"}), 401

            return f(*args, **kwargs)
        return wrapper
    return decorator
