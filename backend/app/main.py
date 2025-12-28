from fastapi import FastAPI
from .db import get_db

app = FastAPI(title="OctoFit Tracker API")


@app.get("/")
async def root():
    return {"message": "OctoFit Tracker API is up"}


@app.get("/health")
async def health():
    # Simple DB check (pings server)
    db = get_db()
    try:
        db.command("ping")
        status = "ok"
    except Exception:
        status = "error"
    return {"status": status}
