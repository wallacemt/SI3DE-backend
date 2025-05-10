from flask import Flask
from flask_cors import CORS
from routes.authRoutes import auth_bp
from routes.userRoutes import user_bp
app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": ["http://localhost:5173", "http://192.168.248.202:5173"]}}, supports_credentials=True)

app.register_blueprint(auth_bp)
app.register_blueprint(user_bp)

if __name__ == "__main__":
    app.run(debug=True)

