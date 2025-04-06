# Contacts API

This is a simple REST API for managing contacts. Built with FastAPI, PostgreSQL, SQLAlchemy, and Pydantic.

## Features

- Create, read, update, and delete contacts
- Search by first name, last name, or email
- Get contacts with upcoming birthdays in the next 7 days
- Async support with PostgreSQL via `asyncpg`
- Interactive Swagger docs

## Technologies

- FastAPI
- SQLAlchemy (async)
- PostgreSQL
- Pydantic v2
- Uvicorn

## Getting Started

### 1. Clone the repo

```bash
git clone https://github.com/yourusername/contacts-api.git
cd contacts-api
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

Or manually:

```bash
pip install fastapi sqlalchemy asyncpg psycopg2-binary uvicorn pydantic[email]
```

### 3. Set up the database

Make sure PostgreSQL is running and create the database `contacts_db`.

Update `DATABASE_URL` in `app/database.py` if needed:

```python
DATABASE_URL = "postgresql+asyncpg://postgres:<your_password>@localhost:5432/contacts_db"
```

### 4. Run the app

```bash
uvicorn app.main:app --reload
```

### 5. Open docs

- Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- ReDoc: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---
