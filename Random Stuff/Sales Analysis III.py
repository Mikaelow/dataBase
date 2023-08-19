import pandas as pd

def sales_analysis(product: pd.DataFrame, sales: pd.DataFrame) -> pd.DataFrame:
    return 


data = [[1, 'S8', 1000], [2, 'G4', 800], [3, 'iPhone', 1400]]
Product = pd.DataFrame(data, columns=['product_id', 'product_name', 'unit_price']).astype(
    {'product_id':'Int64', 'product_name':'object', 'unit_price':'Int64'})

data = [[1, 1, 1, '2019-01-21', 2, 2000], [1, 2, 2, '2019-02-17', 1, 800],
        [2, 2, 3, '2019-06-02', 1, 800], [3, 3, 4, '2019-05-13', 2, 2800]]
Sales = pd.DataFrame(data, columns=['seller_id', 'product_id', 'buyer_id', 'sale_date', 'quantity', 'price']).astype(
    {'seller_id':'Int64', 'product_id':'Int64', 'buyer_id':'Int64', 'sale_date':'datetime64[ns]', 'quantity':'Int64', 'price':'Int64'})