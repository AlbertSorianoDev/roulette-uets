from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.openapi.docs import get_swagger_ui_html
from fastapi.openapi.utils import get_openapi

from src.core.config.database import Base, engine
from src.api.v1.app import api_v1

tags_metadata = [
    {
        "name": "v1",
        "description": "API version 1, check link on the right",
        "externalDocs": {
            "description": "sub-docs",
            "url": "/api/v1/docs",
        },
    },
    {
        "name": "v2",
        "description": "API version 2, check link on the right",
        "externalDocs": {
            "description": "sub-docs",
            "url": "/api/v2/docs",
        },
    },
]

app = FastAPI(openapi_tags=tags_metadata)
app.title = "Roulette UETS Service"
app.version = "0.0.1"

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/api/v1", api_v1)

Base.metadata.create_all(bind=engine)


@app.get("/", tags=["Index"], include_in_schema=False)
async def index():
    return JSONResponse(
        content={"message": "Welcome to Roulette UETS Service"}, status_code=200
    )


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
