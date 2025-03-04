import os
from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import chatbot

# ✅ Load environment variables (inside or outside Docker)
load_dotenv()

# ✅ Debugging: Ensure API Key is loaded
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError(
        "❌ ERROR: OPENAI_API_KEY is missing! Please check your .env file or Docker environment."
    )

print("🔹 Loaded API_URL:", os.getenv("API_URL"))

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # ✅ Allow all origins inside Docker
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(chatbot.router, prefix="/api", tags=["Chatbot"])


@app.get("/")
def home():
    return {"message": "Welcome to Scidyllics Backend 🚀"}
