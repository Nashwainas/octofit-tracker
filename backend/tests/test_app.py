import sys
import os
# Ensure the backend package is importable when pytest runs from workspace root
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.main import app


def test_root():
    # FastAPI TestClient not required here — just ensure app import works
    assert app.title == "OctoFit Tracker API"
