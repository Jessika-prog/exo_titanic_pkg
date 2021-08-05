from fastapi import FastAPI
import joblib
import random
import pandas as pd
import uvicorn

from titanic_pkg.ml import ML

# from typing import optional
from pydantic import BaseModel

app = FastAPI()

@app.get('/')
async def get_root():
    return {'message': 'Welcome to the dead or alive API '}


model = joblib.load('DeadOrAlive.joblib')
# prediction= ML()

# class Passenger(BaseModel):
#     pclass:int
#     sex:str
#     age:float
#     fare:float
#     embarked:str
#     who:str
#     alone:bool

# def create_random_passenger():
#     passenger_dict = {'pclass' : [random.randint(1,3)],
#     'sex' : [random.choice(['male','female'])],
#     'age' : [random.uniform(0.42,80)],
#     'fare' : [random.uniform(0,500)],
#     'embarked' : [random.choice(['S','C','Q'])],
#     'who' : [random.choice(['child','man','woman'])],
#     'alone' : [random.choice([True, False])]}
#     return  pd.DataFrame(passenger_dict)


@app.get('/{passenger_info}')
async def death_detector(passenger_info:str):
    pass_info_title= ['pclass','sex','age','fare','embarked','who','alone']
    pass_info_list = passenger_info.split('&')
    df_passenger=pd.DataFrame()
    i=0
    for info in pass_info_title:
        df_passenger.at[0,info] = pass_info_list[i]
        i+=1
        
    # pass_info_list = passenger_info.split('&')
    # pclass = int(pass_info_list[0])
    # sex = str(pass_info_list[1])
    # age = float(pass_info_list[2])
    # fare = float(pass_info_list[3])
    # embarked = str(pass_info_list[4])
    # who = str(pass_info_list[5])
    # alone = bool(pass_info_list[6])
    # passenger = pd.DataFrame(columns=['pclass','sex','age','fare','embarked','who','alone'],pclass,sex,)
    #return{ 'pass info': pclass,'sex':sex,'age':age,'fare': fare,'embarked':embarked,'who':who,'alone':alone}
    # passenger_dict = {'pclass' : [pclass],
    # 'sex' : [sex],
    # 'age' : [age],
    # 'fare' : [fare],
    # 'embarked' : [embarked],
    # 'who' : [who],
    # 'alone' : [alone]}
    # return{'passenger infos ':passenger_dict}
    # passenger_dict=create_random_passenger()
    #passenger= pd.DataFrame(passenger_dict)
    result = model.predict(df_passenger)
    return {'état du passager à la fin de la croisiere':result}

# @app.get('/prediction_path/{passenger}')
# async def death_detector(pclass=1,sex='female',age=33,fare=45,embarked='S',who='child',alone=True):
#     passenger_dict = {'pclass' :[int(pclass)],
#     'sex' : [sex],
#     'age' : [int(age)],
#     'fare' : [int(fare)],
#     'embarked' : [embarked],
#     'who' : [who],
#     'alone' : [alone]}
#     passenger= pd.DataFrame(passenger_dict)
#     result = prediction.model_predict_test(passenger)
#     return {'response':result}


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)