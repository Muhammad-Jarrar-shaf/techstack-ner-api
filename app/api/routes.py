from fastapi import APIRouter

from app.schemas.ner_schema import (
    PredictionRequest,
    PredictionResponse,
    EntityResponse,
)

from app.services.custom_inference import predict


router = APIRouter()


@router.get("/")
def health_check():
    return {
        "status": "healthy",
        "service": "Tech Stack NER API",
    }


@router.post(
    "/predict",
    response_model=PredictionResponse,
)
def predict_entities(
    request: PredictionRequest,
):
    predictions = predict(request.text)

    entities = [
        EntityResponse(**entity)
        for entity in predictions
    ]

    return PredictionResponse(
        entities=entities,
    )