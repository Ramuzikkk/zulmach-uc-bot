from fastapi import FastAPI
from .database import engine, Base


app = FastAPI(
    title="ZULMACH UC BOT API",
    version="1.0.0"
)


@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


@app.get("/")
def home():
    return {
        "status": "ok",
        "project": "ZULMACH UC BOT"
    }
