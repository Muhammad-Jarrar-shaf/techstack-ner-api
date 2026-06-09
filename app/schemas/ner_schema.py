from pydantic import BaseModel


class PredictionRequest(BaseModel):
    text: str


class EntityResponse(BaseModel):
    text: str
    label: str
    start: int
    end: int


class PredictionResponse(BaseModel):
    entities: list[EntityResponse]