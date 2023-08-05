import pandas as pd
import numpy as np

def rearrange_products_table(products: pd.DataFrame) -> pd.DataFrame:
    products = products.fillna(0)
    pivot_table = pd.pivot_table(products, index='product_id', columns='store1', values='store1', aggfunc='mean')    
    return pivot_table

Products = pd.DataFrame(
    [['0', '95', '100', '105'],
    ['1', '70', None, '80']],
    columns=['product_id', 'store1', 'store2', 'store3']).astype(
    {'product_id':'int64', 'store1':'int64', 'store2':'int64', 'store3':'int64'})
print(rearrange_products_table(Products))