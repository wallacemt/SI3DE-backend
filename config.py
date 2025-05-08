import os
from dotenv import load_dotenv

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")
DB_NAME = "test"
JWT_SECRET = os.getenv("JWT_SECRET")
