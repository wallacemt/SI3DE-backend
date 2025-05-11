from flask_restx import Namespace, fields

auth_ns = Namespace('auth', description='Autenticação de usuários')

login_model = auth_ns.model('LoginModel', {
    'email': fields.String(required=True, example='aluno@aluno.uniruy.edu.br'),
    'password': fields.String(required=True, example='123456')
})

login_response = auth_ns.model('LoginResponse', {
    'nome': fields.String,
    'email': fields.String,
    'role': fields.String,
    'isFullProfile': fields.Boolean,
    'jwtToken': fields.String,
    'acessAt': fields.DateTime,
})
