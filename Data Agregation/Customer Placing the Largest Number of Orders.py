import pandas as pd

def largest_orders(orders: pd.DataFrame) -> pd.DataFrame:
    orders = orders.groupby('customer_number')['order_number'].count().reset_index()
    orders.sort_values(by='order_number',ascending=False,inplace=True)
    return orders.iloc[:1,[0]]


data = [[1, 1], [2, 2], [3, 3], [4, 3]]
orders = pd.DataFrame(data, columns=['order_number', 'customer_number']).astype(
    {'order_number':'Int64', 'customer_number':'Int64'})

print(largest_orders(orders))