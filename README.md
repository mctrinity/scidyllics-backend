# Scidyllics Backend - FastAPI

## 🚀 Overview
Scidyllics Backend is a FastAPI-based REST API designed to handle backend operations efficiently. It includes database integration, authentication, and scalable API endpoints.

## 📂 Project Structure
```
scidyllics-backend/
├── app/
│   ├── main.py           # FastAPI application entry point
│   ├── routes/           # API routes
│   │   ├── users.py      # User-related endpoints
│   │   ├── auth.py       # Authentication endpoints
│   ├── models.py         # SQLAlchemy models
│   ├── schemas.py        # Pydantic models (data validation)
│   ├── services/         # Business logic (e.g., auth services)
│   ├── db.py             # Database connection setup
│   ├── config.py         # Application configuration
│   ├── dependencies.py   # Shared dependencies
├── .env                  # Environment variables (excluded from git)
├── requirements.txt      # Python dependencies
├── Dockerfile            # Docker configuration
├── .gitignore            # Ignored files & directories
├── README.md             # Documentation
```

## 🛠️ Setup Instructions

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/your-username/scidyllics-backend.git
cd scidyllics-backend
```

### 2️⃣ Create & Activate Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Configure Environment Variables
Create a `.env` file:
```
DATABASE_URL=postgresql://user:password@localhost/dbname
SECRET_KEY=your-secret-key
```

### 5️⃣ Run the FastAPI Server
```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```

### 6️⃣ API Documentation
Once the server is running, visit:
- **Swagger UI:** [http://localhost:8000/docs](http://localhost:8000/docs)
- **ReDoc:** [http://localhost:8000/redoc](http://localhost:8000/redoc)

## 🗄️ Database Setup (PostgreSQL)
Ensure PostgreSQL is installed and create a database:
```bash
psql -U postgres -c "CREATE DATABASE scidyllics_db;"
```
Run migrations (if using Alembic):
```bash
alembic upgrade head
```

## 🛡️ Authentication & Security
- Uses **JWT authentication**.
- Secure CORS settings in `main.py`.

## 🧪 Running Tests
Install pytest and run tests:
```bash
pip install pytest
pytest
```

## 🚀 Deployment Guide (Docker)
Build and run the Docker container:
```bash
docker build -t scidyllics-backend .
docker run -p 8000:8000 scidyllics-backend
```

## 📌 Contributing
1. Fork the repository
2. Create a feature branch (`git checkout -b feature-name`)
3. Commit your changes (`git commit -m "Add feature"`)
4. Push to your branch (`git push origin feature-name`)
5. Open a Pull Request

