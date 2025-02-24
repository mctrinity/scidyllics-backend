# 1️⃣ Use an official lightweight Python image
FROM python:3.9-slim

# 2️⃣ Set the working directory inside the container
WORKDIR /app

# 3️⃣ Copy dependency files first (to leverage Docker cache)
COPY requirements.txt ./

# 4️⃣ Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# 5️⃣ Copy the rest of the application files
COPY . .

# 7️⃣ Expose port 8000 for FastAPI
EXPOSE 8000

# 8️⃣ Start FastAPI using Uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
