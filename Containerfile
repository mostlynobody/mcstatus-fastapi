FROM python:3.12.7-bookworm as builder

RUN pip install poetry

ENV POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_IN_PROJECT=1 \
    POETRY_VIRTUALENVS_CREATE=1 \
    POETRY_CACHE_DIR=/tmp/poetry_cache

WORKDIR /mcstatus-fastapi

COPY pyproject.toml poetry.lock ./
RUN touch README.md

RUN poetry install --no-root && rm -rf $POETRY_CACHE_DIR

FROM python:3.12.7-slim-bookworm as runtime

ENV VIRTUAL_ENV=/mcstatus-fastapi/.venv \
    PATH="/mcstatus-fastapi/.venv/bin:$PATH"

COPY --from=builder ${VIRTUAL_ENV} ${VIRTUAL_ENV}

COPY app ./app

ENTRYPOINT ["python", "-m", "app.main"]

LABEL maintainer="mostlynobody <tycho@mostlynobody.com>>"
LABEL name="mcstatus-fastapi"
LABEL description="This is a Container for mcstatus-fastapi."
LABEL version="0.1.0"
LABEL org.opencontainers.image.licenses="MIT"
LABEL org.opencontainers.image.source="https://github.com/mostlynobody/mcstatus-fastapi"