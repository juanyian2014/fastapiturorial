from typing import List,Union
from fastapi import FastAPI
from pydantic import BaseModel, json, Field 
from functools import reduce

app = FastAPI()


class order(List):
    id: int
    item: str
    quantity: int
    price: float
    status: str


class Item(BaseModel):
    orders: order
    criterion: str
    

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/solution")
def process( params: Item):
    return process_orders(params.orders,params.criterion)
   

def process_orders(orders,criterion):
    filtered = orders   
    if criterion != 'all':
       filtered = list(filter(lambda x: x['status'] == criterion, filtered))
    
    
    negative_exist = filter( lambda x: x['price'] < 0,  filtered) 
    if len(list(negative_exist)) > 0:
       return " there are negative element in data "

    return round(reduce( lambda tot,v: tot + v['price'],filtered,0),2)