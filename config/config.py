import os
from dotenv import load_dotenv

load_dotenv()

FRONTEND_URL = os.getenv("PATH_FRONTEND")
MONGO_URI = os.getenv("MONGO_URI")
DB_NAME = "test"
JWT_SECRET = os.getenv("JWT_SECRET")
