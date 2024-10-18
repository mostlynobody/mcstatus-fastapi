import uvicorn
from fastapi import FastAPI
from app.core.config import settings

app = FastAPI(title=settings.PROJECT_NAME, version=settings.PROJECT_VERSION)

@app.get("/")
def read_root():
    return {"message": "Welcome to FastAPI!"}


def start():
    """Launched with `poetry run start` at root level"""
    uvicorn.run("app.main:app", host="0.0.0.0", port=8080, reload=False)
    # TODO add ENV config, see https://www.uvicorn.org/

def start_dev():
    """Launched with `poetry run start` at root level"""
    uvicorn.run("app.main:app", host="127.0.0.1", port=8080, reload=True)
