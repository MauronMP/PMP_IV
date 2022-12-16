FROM bitnami/python:3.9

RUN mkdir -p /app/test

ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

RUN export PYTHONDONTWRITEBYTECODE=1

RUN pip install --upgrade pip poetry
COPY pyproject.toml poetry.lock ./
RUN poetry install && rm ./pyproject.toml ./poetry.lock   

WORKDIR /app/test/
RUN chown -R 1001:1001 /app/

ENTRYPOINT [ "inv", "test" ]