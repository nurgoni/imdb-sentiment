from pydantic import BaseModel

class TextToPredict(BaseModel):
    text: str

class PredictRespons(BaseModel):
    prediction: str
    probability: float