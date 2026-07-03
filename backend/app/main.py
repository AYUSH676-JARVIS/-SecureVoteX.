from fastapi import FastAPI

from app.api.v1.auth import router as auth_router

app = FastAPI(
    title="SecureVoteX",
    version="1.0.0",
    description="Blockchain-based Election Security Platform",
)

app.include_router(auth_router)


@app.get("/")
def root():
    return {
        "status": "running",
        "application": "SecureVoteX",
        "version": "1.0.0",
    }