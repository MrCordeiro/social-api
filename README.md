# Social API

FastAPI tutorial that mimics a social network API

## Installation

```bash
pip install poetry
poetry install
```

## Usage

Start the web server:

```bash
uvicorn app.main:app --reload
```

To start running Alembic:

```bash
alembic init DIRETORY_NAME
```

When making a change to the database, run:

```bash
alembic revision --autogenerate -m "MESSAGE"
```

To run an specific change:

```bash
alembic upgrade REVISION_ID
```

To run up to the latest revision:

```bash
alembic upgrade head
```
