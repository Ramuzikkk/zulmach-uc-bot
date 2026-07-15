from fastapi import FastAPI

app = FastAPI(
    title="ZULMACH UC BOT API",
    version="1.0.0"
)

@app.get("/")
def home():
    return {
        "status": "ok",
        "project": "ZULMACH UC BOT"
    }

@app.get("/health")
def health():
    return {
        "status": "healthy"
    }
