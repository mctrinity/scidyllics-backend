from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Initialize FastAPI app
app = FastAPI(
    title="Scidyllics Backend",
    description="API for Scidyllics project",
    version="1.0.0",
)

# CORS settings (Update origins if needed)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change this to specific frontend URLs for security
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Root endpoint
@app.get("/")
def home():
    return {"message": "Welcome to Scidyllics Backend 🚀"}


# Include API routes (to be added later)
# from app.routes import users, auth, items
# app.include_router(users.router, prefix="/users", tags=["Users"])
# app.include_router(auth.router, prefix="/auth", tags=["Authentication"])


# Health check endpoint
@app.get("/health")
def health_check():
    return {"status": "ok"}


# Run the app (only for local development, use `uvicorn` in production)
if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)
