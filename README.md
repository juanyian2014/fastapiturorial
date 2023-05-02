
With the use of FastApi, the solution to the problem of the exercise proposed in Coding exercise is created.

  Where these are the requirements to be met specifically

Implement a single function named process_orders that receives a list of orders and a filter criteria. The function should filter the orders based on the criteria and return the total revenue for the filtered orders. The function signature should be as follows:
def process_orders(orders, criteria):
     pass
​
The input parameter orders is a list of dictionaries, where each dictionary represents an order with the following keys:
id: an integer representing the order ID
item: a string representing the item name
quantity: an integer representing the number of items in the order
price: a number representing the price per item
status: a string representing the order status, which can be either completed, pending, or canceled
The criteria is a string that indicates the filter to be applied to the orders. The function should support the following criteria:
completed: Only consider orders with the status completed.
pending: Only consider orders with the status pending.
cancelled: Only consider orders with the status cancelled.
all: Consider all orders, regardless of their status

To provide a solution, a class was created to receive data and to facilitate the work, the FastApi module is used.

this class

class order(List):
     id: int
     item:str
     amount: int
     price: float
     status: str

It is the one that maintains the structure that the data that will contain the list must have, since another class must be used that contains the list of data and the selection criteria for the moment of carrying out the calculations.

class that performs this function
class Item(BaseModel):
     orders: order
     criteria: str

With the aid of these two classes and the following method, the objective is achieved

@app.post("/solution")
def process( params: Item):
     return process_orders(params.orders,params.criterion)

receiving in the API the data from the JSON shipment are supplied to the function or method in charge of converting it into the desired results

def process_orders(orders, criteria):
     filtered = orders
     if criteria != 'all':
        filtered = list(filter(lambda x: x['status'] == criteria, filtered))
    
    
     negative_exist = filter( lambda x: x['price'] < 0, filtered)
     if len(list(negative_exist)) > 0:
        return " there are negative elements in data "

     return round(reduce( lambda tot,v: tot + v['price'],filtered,0),2)


  This file provides a solution to this problem.
