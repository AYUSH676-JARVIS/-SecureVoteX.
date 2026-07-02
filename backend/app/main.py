from fastapi import FastAPI

app = FastAPI(
    title="SecureVoteX API",
    version="1.0.0",
)


@app.get("/")
def root():
    return {
        "message": "SecureVoteX Backend Running"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }