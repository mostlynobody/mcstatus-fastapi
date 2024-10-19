import uvicorn
from fastapi import FastAPI
from starlette import status, responses

from app.core.config import settings
from app.core.minecraft import init_mc_server

app = FastAPI(title=settings.project_name, version=settings.project_version)
mc_server = init_mc_server(settings)


@app.get('/')
def healthiness():
    return responses.Response(status_code=status.HTTP_204_NO_CONTENT)


@app.get('/status')
def server_status():
    try:
        response = mc_server.status()
    except ConnectionRefusedError:
        return responses.Response(status_code=status.HTTP_503_SERVICE_UNAVAILABLE)

    return responses.JSONResponse(status_code=status.HTTP_200_OK, content=response.raw)


def main():
    uvicorn.run('app.main:app',
                host=settings.uvicorn_host,
                port=settings.uvicorn_port,
                reload=settings.uvicorn_reload,
                log_level=settings.uvicorn_log_level)


if __name__ == "__main__":
    main()
