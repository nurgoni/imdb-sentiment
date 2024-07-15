import joblib
from app import preprocessing as pp
from app import schemas
from fastapi import FastAPI


with open("app/models/sentiment_model_pipeline.pkl", "rb") as f:
    model = joblib.load(f)

app = FastAPI(
    title="Sentiment Model API",
    version="0.1"
)

@app.post("/predict", response_model=schemas.PredictRespons)
def predict(review: schemas.TextToPredict):
    """
    
    """
    cleaned_review = pp.text_cleaning(review.text)

    # prediction
    prediction = model.predict([cleaned_review])
    output = int(prediction[0])

    # predict proba
    probas = model.predict_proba([cleaned_review])
    output_proba = "{:.2f}".format(float(probas[:, output]))

    # output dictionary
    sentiments = {0: "Negative", 1: "Positive"}

    return {"prediction": sentiments[output], "probability": output_proba}