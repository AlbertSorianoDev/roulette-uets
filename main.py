from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware

from src.core.config.database import Base, engine
from src.api.v1.routers.main_router import api_v1_router

app = FastAPI()
app.title = "Roulette UETS Service"
app.version = "0.0.1"

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_v1_router)

Base.metadata.create_all(bind=engine)


@app.get("/", tags=["Index"])
async def index():
    return JSONResponse(
        content={"message": "Welcome to Roulette UETS Service"}, status_code=200
    )


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
