from pydantic import BaseModel

class TextToPredict(BaseModel):
    text: str