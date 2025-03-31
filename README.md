# 🚀 NASA Near-Earth Objects Project

[![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-green)](https://fastapi.tiangolo.com/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-15-blue)](https://www.postgresql.org/)
[![Alembic](https://img.shields.io/badge/Alembic-Migrations-orange)](https://alembic.sqlalchemy.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

This project utilizes NASA's [Asteroids - NeoWs](https://api.nasa.gov/) (Near Earth Object Web Service) API to retrieve and store information about asteroids approaching Earth. The goal was to gain hands-on experience working with **FastAPI**, **SQLAlchemy**, **Pydantic**, **PostgreSQL**, and **Alembic** for database migrations.

---

## 🧠 What I Learned

- How to build RESTful APIs using FastAPI
- Modeling complex and dynamic JSON schemas with Pydantic
- Persisting external API data into a PostgreSQL database
- Implementing database migrations with Alembic
- Structuring a clean and modular FastAPI project
- Error handling and data validation for external APIs

---

## 🛠️ Tech Stack

| Tool        | Description                                |
|-------------|--------------------------------------------|
| FastAPI     | Python web framework for building APIs     |
| SQLAlchemy  | ORM for database modeling and queries      |
| Pydantic    | Data validation and parsing with Python    |
| PostgreSQL  | Relational database for persistent storage |
| Alembic     | Database migration tool for SQLAlchemy     |
| NASA NeoWs  | External REST API for asteroid data        |

---

## 📦 Features

- 🔭 Fetch & store asteroid data from NASA's NeoWs API
- 📅 Search asteroids by approach date
- 🔎 View detailed info for specific objects
- 💾 Save queries to a PostgreSQL database
- 🔄 Database migrations with Alembic
- ✅ Includes data validation & basic error handling

---

## ▶️ Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/your-username/nasa-project.git
cd nasa-project
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Set up the database

Before running the API, apply database migrations using Alembic:

```bash
alembic upgrade head
```

### 4. Run the API server

```bash
uvicorn main:app --reload
```

### 5. Open API Docs

Visit the interactive Swagger docs:  
📍 `http://localhost:8000/docs`

---

## 📁 Project Structure

```
nasa-api-project/
│
├── nasa-project/
│   ├── main.py              # FastAPI app entry point
│   ├── models.py            # SQLAlchemy models
│   ├── schemas.py           # Pydantic schemas
│   ├── database.py          # DB connection setup
│   ├── alembic/             # Alembic migrations
│   ├── migrations/          # Database migration scripts
│   ├── requirements.txt     # Packages
│
└── README.md
```

---

## 🔗 Example Endpoints

- `/asteroid/{id}` : Retrieve information about a specific asteroid
- `/asteroids` : Retrieve paginated asteroid data
- `/asteroids/date_range` : Fetch Near-Earth Objects within a given date range

---

## 🌌 Credits

- 🛰️ Data provided by [NASA NeoWs API](https://api.nasa.gov/)
- 💡 Inspired by curiosity about space and backend development

---

## 📄 License

This project is licensed under the MIT License.

