# OctoFit Tracker — Backend

## Setup (local)

1. Create virtualenv:

```bash
python3 -m venv /workspaces/octofit-tracker/backend/venv
```

2. Activate & install:

```bash
source /workspaces/octofit-tracker/backend/venv/bin/activate
pip install -r /workspaces/octofit-tracker/backend/requirements.txt
```

3. Copy `.env.example` to `.env` and edit MongoDB settings.

4. Run:

```bash
# from workspace root (do not change directories in scripts)
source /workspaces/octofit-tracker/backend/venv/bin/activate
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

### MongoDB

- Make sure MongoDB is running locally (for example: `ps aux | grep mongod`).
- Use `mongosh` or your preferred Mongo client and set `MONGODB_URI` and `MONGODB_DB` in a `.env` (copy `.env.example`).
- The app uses `pymongo` and reads `.env` from the `backend/` folder at startup.
