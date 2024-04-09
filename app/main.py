from fastapi import FastAPI
from pydantic import BaseModel
from app.model.model import predict_pipline


app = FastAPI()



class TextIn(BaseModel):
    text: str

class PredictionOut(BaseModel):
    language: str




@app.get('/')
def home():
    return {"Home"}


@app.post('/predict', response_model = PredictionOut)
def predict(payload: TextIn):
    language = predict_pipline(payload.text)
    return {'language': language}