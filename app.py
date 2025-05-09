from flask import Flask
from flask_cors import CORS
from routes.routes import auth_bp

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "http://localhost:5173"}}, supports_credentials=True)

app.register_blueprint(auth_bp)

if __name__ == "__main__":
    app.run(debug=True)

