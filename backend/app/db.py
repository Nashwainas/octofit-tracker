from pymongo import MongoClient
from dotenv import load_dotenv
import os

# Load environment variables from backend/.env if present
here = os.path.dirname(os.path.dirname(__file__))
dotenv_path = os.path.join(here, ".env")
load_dotenv(dotenv_path=dotenv_path)

MONGODB_URI = os.getenv("MONGODB_URI", "mongodb://localhost:27017")
MONGODB_DB = os.getenv("MONGODB_DB", "octofit")

# Create a single MongoClient for the app (thread-safe)
client = MongoClient(MONGODB_URI)
db = client[MONGODB_DB]


def get_db():
    """Return the database instance."""
    return db
