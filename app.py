from flask import Flask
from flask_cors import CORS
from routes.authRoutes import auth_bp
from routes.vagasRoutes import vagas_bp
from routes.insightsRoutes import insights_bp
from routes.userRoutes import user_bp
from config.config import FRONTEND_URL
from flask import send_from_directory


app = Flask(__name__, static_folder="static/swagger-ui")
CORS(app, resources={r"/*": {"origins": ["http://192.168.248.202:5173", FRONTEND_URL]}}, supports_credentials=True)


@app.route("/docs")
def swagger_ui():
    return send_from_directory(app.static_folder, "index.html")

@app.route("/swagger-ui/<path:filename>")
def swagger_ui_static(filename):
    return send_from_directory(os.path.join(app.static_folder), filename)

@app.route("/swagger.json")
def swagger_json():
    return send_from_directory(app.static_folder, "swagger.json")

app.register_blueprint(auth_bp)
app.register_blueprint(user_bp)
app.register_blueprint(vagas_bp)
app.register_blueprint(insights_bp)
if __name__ == "__main__":
   import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)


