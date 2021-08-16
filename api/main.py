import pandas as pd
from fastapi import FastAPI, Form
from fastapi.middleware.cors import CORSMiddleware

import uvicorn

from titanic_pkg.ml import ML

app = FastAPI()

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://127.0.0.1:5500",
    "http://localhost:8000",
    "https://deadtitanic.azurewebsites.net/",
    "https://jessika-prog.github.io/",
    "https://jessika-prog.github.io/exo_titanic_pk/#resultat:1"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get('/')
async def get_root():
    return {'message': 'Welcome to titanic survivor prediction app'}


@app.post("/passenger_dict/")
async def passenger_dict(pclass: int = Form(...),
                         sex: str = Form(...),
                         age: float = Form(...),
                         fare: float = Form(...),
                         embarked: str = Form(...),
                         who: str = Form(...),
                         alone: bool = Form(...)):
    passengers = {
        'pclass': [pclass],
        'sex': [sex],
        'age': [age],
        'fare': [fare],
        'embarked': [embarked],
        'who': [who],
        'alone': [alone]
    }
    X = pd.DataFrame(passengers)
    prediction = ML()
    pred = prediction.model_predict_test(X)
    if pred[0][0] == 0:
        result = 'No'
    else:
        result = 'Yes'
    return  {'result': result}

if __name__ == "__main__":
    uvicorn.run("main:app", host="localhost", port=8000, reload=True)
