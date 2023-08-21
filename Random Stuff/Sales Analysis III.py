# Write a solution to report the products that were only sold in the first quarter of 2019. That is, between 2019-01-01 and 2019-03-31 inclusive.
# Return the result table in any order.
# The result format is in the following example.
 
import pandas as pd

def sales_analysis(product: pd.DataFrame, sales: pd.DataFrame) -> pd.DataFrame:
    saled_in_first_quarter = sales[sales['sale_date'].between('2019-01-01','2019-03-31')]
    saled_in_all_others_quarter = sales[(sales['sale_date']>'2019-03-31') | (sales['sale_date']<'2019-01-01')]
    correct_id = pd.merge(saled_in_first_quarter, saled_in_all_others_quarter, how='left', on='product_id')
    correct_id = correct_id[correct_id['seller_id_y'].isna()][['product_id']]
    merged_tbl = pd.merge(correct_id,product,on='product_id',how='left')[['product_id','product_name']].drop_duplicates()
    return merged_tbl


data = [[1, 'S8', 1000], [2, 'G4', 800], [3, 'iPhone', 1400]]
Product = pd.DataFrame(data, columns=['product_id', 'product_name', 'unit_price']).astype(
    {'product_id':'Int64', 'product_name':'object', 'unit_price':'Int64'})

data = [[1, 1, 1, '2019-01-21', 2, 2000], [1, 2, 2, '2019-02-17', 1, 800],
        [2, 2, 3, '2019-06-02', 1, 800], [3, 3, 4, '2019-05-13', 2, 2800]]
Sales = pd.DataFrame(data, columns=['seller_id', 'product_id', 'buyer_id', 'sale_date', 'quantity', 'price']).astype(
    {'seller_id':'Int64', 'product_id':'Int64', 'buyer_id':'Int64', 'sale_date':'datetime64[ns]', 'quantity':'Int64', 'price':'Int64'})

print(sales_analysis(Product,Sales))