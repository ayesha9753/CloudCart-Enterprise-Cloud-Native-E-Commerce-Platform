# 🛒 CloudCart – Enterprise Cloud-Native E-Commerce Platform

CloudCart is a cloud-native e-commerce backend application built using modern backend and DevOps technologies. The project demonstrates real-world software development practices including REST APIs, authentication, containerization, CI/CD, database migrations, and cloud deployment.

## 🚀 Live Demo

- **Live API:** https://cloudcart-api.onrender.com
- **Swagger Documentation:** https://cloudcart-api.onrender.com/docs
- **GitHub Repository:** https://github.com/ayesha9753/CloudCart-Enterprise-Cloud-Native-E-Commerce-Platform

---

# ✨ Features

- User Registration
- User Login
- JWT Authentication
- Protected APIs
- Product CRUD Operations
- PostgreSQL Database
- SQLAlchemy ORM
- Alembic Database Migrations
- Docker & Docker Compose
- GitHub Actions CI
- Render Deployment
- Interactive Swagger API Documentation

---

# 🛠 Tech Stack

- Python 3.13
- FastAPI
- PostgreSQL
- SQLAlchemy
- Alembic
- JWT (python-jose)
- Passlib (bcrypt)
- Docker
- Docker Compose
- GitHub Actions
- Render

---

# 📂 Project Structure

```text
CloudCart-Enterprise-Cloud-Native-E-Commerce-Platform/
│
├── .github/
│   └── workflows/
├── app/
│   └── backend/
│       ├── app/
│       ├── alembic/
│       ├── Dockerfile
│       ├── docker-compose.yml
│       └── requirements.txt
├── kubernetes/
├── terraform/
├── helm/
└── README.md
```

---

# 🔐 Authentication

CloudCart uses JWT (JSON Web Token) authentication.

### Public Endpoints

- POST /auth/signup
- POST /auth/login

### Protected Endpoints

- POST /products
- PUT /products/{id}
- DELETE /products/{id}

---

# 📦 Installation

```bash
git clone https://github.com/ayesha9753/CloudCart-Enterprise-Cloud-Native-E-Commerce-Platform.git

cd CloudCart-Enterprise-Cloud-Native-E-Commerce-Platform/app/backend

docker compose up --build
```

---

# 🗄 Database Migrations

```bash
docker compose exec backend alembic upgrade head
```

---

# 🧪 API Documentation

Swagger UI:

https://cloudcart-api.onrender.com/docs

---

# 🚀 Deployment

Backend is deployed on **Render**.

Database is hosted on **Render PostgreSQL**.

---

# 🔮 Future Improvements

- Categories
- Shopping Cart
- Orders
- Payment Integration
- Kubernetes Deployment
- Terraform Infrastructure
- Helm Charts
- ArgoCD GitOps
- Prometheus & Grafana Monitoring
- Loki Logging

---

# 👩‍💻 Author

**Ayesha Imran**

- GitHub: https://github.com/ayesha9753
- LinkedIn: https://www.linkedin.com/in/ayesha-imran-3a5265369/