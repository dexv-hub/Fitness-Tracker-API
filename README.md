## Fitness Tracker API

A RESTful API for tracking fitness-related data including nutrition, workouts, sleep, water intake, and body metrics.

The project is built with Django REST Framework and designed with clean architecture, user-based data isolation, and JWT authentication.
Deployed to production using Render with PostgreSQL.

---

## 🚀 Features

- User authentication with JWT (SimpleJWT)
- Secure user-based data access
- Nutrition & calorie tracking
- Workout tracking
- Sleep, water, and body metrics tracking
- Daily aggregated statistics (calories, macros)
- Swagger / OpenAPI documentation
- Production-ready deployment

---

## 🛠 Tech Stack

- **Python**
- **Django**
- **Django REST Framework**
- **PostgreSQL**
- **JWT Authentication**
- **drf-spectacular (Swagger / OpenAPI)**
- **Gunicorn**
- **Render**

---

## 🌍 Live Demo

- **Swagger UI**:
  https://fitness-tracker-api-3-odkw.onrender.com/api/docs/

- **OpenAPI Schema**:
  https://fitness-tracker-api-3-odkw.onrender.com/api/schema/

---

## 📦 Installation (Local Setup)

```bash
git clone https://github.com/dexv-hub/Fitness-Tracker-API.git
cd Fitness-Tracker-API

python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

pip install -r requirements.txt



## 📚 API Endpoints (Examples)

| Endpoint | Description |
|--------|------------|
| `/api/users/` | User management |
| `/api/nutrition/` | Nutrition tracking |
| `/api/workouts/` | Workout tracking |
| `/api/sleep/` | Sleep tracking |
| `/api/water/` | Water intake |
| `/api/body/` | Body metrics |
| `/api/stats/` | Daily aggregated statistics |


## 🚀 Deployment

The project is deployed on **Render** with:

- Django backend running via **Gunicorn**
- PostgreSQL managed database
- Environment variables for secrets and database credentials
- Automatic deployments from GitHub


## 👤 Author

**Vlad Rybak**
Python Backend Developer

GitHub: https://github.com/dexv-hub
