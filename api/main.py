from fastapi import FastAPI
import random
import pandas as pd
import uvicorn
import os

from titanic_pkg.ml import ML

from typing import Optional, Set
from pydantic import BaseModel

app = FastAPI()

@app.get('/')
async def get_root():
    return {'message': 'Welcome to the dead or alive API '}

model = ML().get_model()

#option 1
@app.get("/prediction/{passenger_info}")
async def death_detector(passenger_info:str):
    pass_info_title= ['pclass','sex','age','fare','embarked','who','alone']
    pass_info_list = passenger_info.split('&')
    df_passenger=pd.DataFrame()
    i=0
    for info in pass_info_title:
        df_passenger.at[0,info] = pass_info_list[i]
        i+=1
    result = model.predict(df_passenger)[0]
    if result == 0 :
        result = 'Dead'
    else :
        result = "Alive"
    return {'état du passager à la fin de la croisiere':result, 'infos passager':passenger_info}

#option 2
@app.get("/prediction_path/")
async def death_detector(pclass=1,sex='female',age=33,fare=45,embarked='S',who='child',alone=True):
    passenger_dict = {'pclass' :[int(pclass)],
    'sex' : [sex],
    'age' : [int(age)],
    'fare' : [int(fare)],
    'embarked' : [embarked],
    'who' : [who],
    'alone' : [alone]}
    passenger= pd.DataFrame(passenger_dict)
    result = model.predict(passenger)[0]
    if result == 0 :
        result = 'Dead'
    else :
        result = "Alive"
    return {'état du passager à la fin de la croisiere':result, 'infos passager':passenger_dict}

# if __name__ == "__main__":
#      uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
        
################# ---- Draft---- #######################

# prediction= ML()

class Passenger(BaseModel):
    pclass:int
    sex:str
    age:float
    fare:float
    embarked:str
    who:str
    alone:bool

# def create_random_passenger():
#     passenger_dict = {'pclass' : [random.randint(1,3)],
#     'sex' : [random.choice(['male','female'])],
#     'age' : [random.uniform(0.42,80)],
#     'fare' : [random.uniform(0,500)],
#     'embarked' : [random.choice(['S','C','Q'])],
#     'who' : [random.choice(['child','man','woman'])],
#     'alone' : [random.choice([True, False])]}
#     return  pd.DataFrame(passenger_dict)
 
class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None
    tags: Set[str] = []


@app.post("/items/", response_model=Item, summary="Create an item")
async def create_item(item: Item):
    """
    Create an item with all the information:

    - **name**: each item must have a name
    - **description**: a long description
    - **price**: required
    - **tax**: if the item doesn't have tax, you can omit this
    - **tags**: a set of unique tag strings for this item
    \f
    :param item: User input.
    """
    return item

