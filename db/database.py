from pymongo import MongoClient
from config.config import MONGO_URI, DB_NAME

client = MongoClient(MONGO_URI)
db = client[DB_NAME]
users_collection = db["users"]
profiles_collection = db["profiles"]
vagas_collection = db["vagas"]
