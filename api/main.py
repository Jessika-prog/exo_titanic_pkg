import pandas as pd
from fastapi import FastAPI
import uvicorn

from titanic_pkg.ml import ML

app = FastAPI()


@app.get('/')
async def get_root():
    return {'message': 'Welcome to titanic survivor prediction app'}

@app.get('/prediction/{passenger}')
async def survive_prediction(passenger:str):
    list_params = passenger.split('&')
    dict_params = {'pclass': [int(list_params[0])],
                      'sex': [list_params[1]],
                      'age': [float(list_params[2])],
                      'fare': [float(list_params[3])],
                      'embarked': [list_params[4]],
                      'who': [list_params[5]],
                      'alone': [bool(list_params[6])]
                      }
    X = pd.DataFrame(dict_params)
    prediction = ML()
    pred = prediction.model_predict_test(X)
    if pred[0][0] == 0:
        result = 'No'
    else:
        result = 'Yes'
    return {'Did you survive ?': result}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=5000, reload=True)


