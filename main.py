from fastapi import FastAPI
from fastapi.responses import JSONResponse
from src.core.config.database import Base, engine

app = FastAPI()
app.title = "Roulette UETS API"
app.version = "0.0.1"

Base.metadata.create_all(bind=engine)


@app.get("/", tags=["Index"])
async def index():
    return JSONResponse(content={"message": "Welcome to UETS API"}, status_code=200)
