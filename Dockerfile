FROM python:3.10-alpine

WORKDIR /app

RUN pip install poetry

COPY pyproject.toml poetry.lock ./

RUN poetry config virtualenvs.create false && poetry install --no-dev

COPY . .

# run the application
CMD ["python3", "src/main.py"]