FROM python:3.8-slim-buster

RUN mkdir -p /app/test

ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

RUN export PYTHONDONTWRITEBYTECODE=1

WORKDIR /app/test/
RUN chown -R 1001:1001 /app/
COPY pyproject.toml .

RUN pip install invoke
RUN pip install poetry

RUN poetry install

ENTRYPOINT [ "inv", "test" ]