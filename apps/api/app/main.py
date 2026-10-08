from fastapi import FastAPI
from app.routes.flights import router as flights_router

app = FastAPI(title="Travel Agent API")
app.include_router(flights_router, prefix="/api/v1")


@app.get("/health")
async def health_check():
    return {"status": "ok"}
