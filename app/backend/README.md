# CloudCart Backend API

CloudCart Backend is built using FastAPI and follows modern backend development practices with JWT authentication, SQLAlchemy ORM, PostgreSQL, Docker, and GitHub Actions.

---

## Features

- JWT Authentication
- User Signup
- User Login
- Product CRUD
- Protected APIs
- SQLAlchemy ORM
- PostgreSQL
- Alembic Migrations
- Docker
- Docker Compose
- GitHub Actions
- Render Deployment

---

## Tech Stack

- FastAPI
- PostgreSQL
- SQLAlchemy
- Alembic
- Docker
- GitHub Actions
- Render

---

## Run Locally

```bash
docker compose up --build
```

API:

```
http://localhost:8000
```

Swagger:

```
http://localhost:8000/docs
```

---

## Production

Live API

https://cloudcart-api.onrender.com

Swagger

https://cloudcart-api.onrender.com/docs

---

## Authentication

Signup

```
POST /auth/signup
```

Login

```
POST /auth/login
```

---

## Product APIs

```
GET /products
POST /products
PUT /products/{id}
DELETE /products/{id}
```

Protected endpoints require JWT Bearer Token.

---

## Author

Ayesha Imran