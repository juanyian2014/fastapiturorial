# Author: Juan Carlos Delgado Gonzalez
 

from typing import List,Union
from fastapi import FastAPI
from pydantic import BaseModel, json, Field 
from functools import reduce

app = FastAPI()

#class definition to receive the data from the post in a list of orders
class order(List):
    id: int
    item: str
    quantity: int
    price: float
    status: str

# class to receive the all data from the post
# this include the list for recieved order and the criterial params for select data in calculation proccess

class Item(BaseModel):
    orders: order
    criterion: str
    

@app.get("/")
def read_root():
    return {"WellCome": "Implementation FastApi for Coding exercise"}


@app.post("/solution")
def process( params: Item):
    return process_orders(params.orders,params.criterion)


# function or method for calculation proccess
# in the case that someone price contain negative value this return message with alert
def process_orders(orders,criterion):
    filtered = orders   
    if criterion != 'all':
       filtered = list(filter(lambda x: x['status'] == criterion, filtered))
    
    
    negative_exist = filter( lambda x: x['price'] < 0,  filtered) 
    if len(list(negative_exist)) > 0:
       return " there are negative element in data "

    return round(reduce( lambda tot,v: tot + v['price'],filtered,0),2)