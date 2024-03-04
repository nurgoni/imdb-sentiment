import joblib
import uvicorn
from app import preprocessing as pp
from fastapi import FastAPI

from os.path import dirname, join, realpath

with open (join(dirname(realpath(__file__)), "models/sentiment_model_pipeline.pkl"), "rb") as f:
    model = joblib.load(f)

app = FastAPI(
    title="Sentiment Model API",
    version="0.1"
)

@app.get("/predict")
def predict(review: str):
    """
    
    """
    cleaned_review = pp.text_cleaning(review)

    # prediction
    prediction = model.predict([cleaned_review])
    output = int(prediction[0])

    # predict proba
    probas = model.predict_proba([cleaned_review])
    output_proba = "{:.2f}".format(float(probas[:, output]))

    # output dictionary
    sentiments = {0: "Negative", 1: "Positive"}

    return {"prediction": sentiments[output], "probability": output_proba}