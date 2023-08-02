import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    resoults = customers[~customers['id'].isin(orders['customerId'])]
    resoults = resoults[['name']]
    resoults.columns=['Customers']
    return resoults


Customers = pd.DataFrame([['1', 'Joe'],
['2', 'Henry'],
['3', 'Sam'],
['4', 'Max']], columns=['id', 'name']).astype({'id':'Int64', 'name':'object'})


Orders = pd.DataFrame([['1', '3'],
['2', '1']], columns=['id', 'customerId']).astype({'id':'Int64', 'customerId':'Int64'})

print(find_customers(Customers,Orders))