import pandas as pd
from fastapi import FastAPI, Form
import uvicorn

from titanic_pkg.ml import ML

app = FastAPI()


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
    return {'Did you survive ?': result}
    # return f'/prediction/{passengers}'


@app.get('/prediction/{passengers}')
async def survive_prediction(passengers:str):
    X = pd.DataFrame(passengers)
    prediction = ML()
    pred = prediction.model_predict_test(X)
    if pred[0][0] == 0:
        result = 'No'
    else:
        result = 'Yes'
    return {'Did you survive ?': result}


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=5000, reload=True)
