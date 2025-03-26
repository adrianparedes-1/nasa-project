# 🚀 NASA Near-Earth Objects Project

[![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-green)](https://fastapi.tiangolo.com/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-15-blue)](https://www.postgresql.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

This project uses NASA's [Asteroids - NeoWs](https://api.nasa.gov/) (Near Earth Object Web Service) API to retrieve and store information about asteroids approaching Earth. The goal was to gain hands-on experience working with **FastAPI**, **SQLAlchemy**, **Pydantic**, and **PostgreSQL**.

---

## 🧠 What I Learned

- How to build RESTful APIs using FastAPI
- Modeling complex and dynamic JSON schemas with Pydantic
- Persisting data from external APIs into a local PostgreSQL database
- Clean architecture and modular project structure
- Error handling and validation for external data

---

## 🛠️ Tech Stack

| Tool        | Description                                |
|-------------|--------------------------------------------|
| FastAPI     | Python web framework for building APIs     |
| SQLAlchemy  | ORM for database modeling and queries      |
| Pydantic    | Data validation and parsing with Python    |
| PostgreSQL  | Relational database for persistent storage |
| NASA NeoWs  | External REST API for asteroid data        |

---

## 📦 Features

- 🔭 Fetch & store asteroid data from NASA's NeoWs API
- 📅 Search asteroids by approach date
- 🔎 View detailed info for specific objects
- 💾 Save queries to a PostgreSQL database
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

### 3. Run the API server

```bash
uvicorn main:app --reload
```

### 4. Open API Docs

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
|   ├── requirements.txt     # Packages
│   └── database.py          # DB connection setup 
│
└── README.md
```

---

## 🔗 Example Endpoints

- `/asteroid/{id}`
- `/asteroids`
- `/asteroids/date_range`

---

## 🌌 Credits

- 🛰️ Data provided by [NASA NeoWs API](https://api.nasa.gov/)
- 💡 Inspired by curiosity about space and backend development

---

## 📄 License

This project is licensed under the MIT License.