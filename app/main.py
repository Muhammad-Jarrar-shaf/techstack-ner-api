from fastapi import FastAPI

from app.api.routes import router


app = FastAPI(
    title="Tech Stack NER API",
    description=(
        "Custom Named Entity Recognition API "
        "for extracting technology-related entities."
    ),
    version="1.0.0",
)


app.include_router(router)