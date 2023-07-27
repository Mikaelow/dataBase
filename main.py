import pandas as pd

def recyclable_and_low_fat_products(products: pd.DataFrame) -> pd.DataFrame:
    filtered_products = products[(products['low_fats'] == 'Y') & (products['recyclable'] == 'Y')]
    return filtered_products[['product_id']]
df = pd.read_csv('C:/Users/User/Desktop/programowanie/IdeaProjects/dataBase/ex1.csv')

rec = recyclable_and_low_fat_products(df)
print(rec)