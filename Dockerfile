FROM python:3.11-bullseye

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir poetry && \
    poetry config virtualenvs.create false && \
    poetry install --no-dev --no-interaction --no-ansi

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
