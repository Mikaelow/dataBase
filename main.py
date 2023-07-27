import pandas as pd
df = pd.read_excel('C:/Users/User/Desktop/programowanie/IdeaProjects/dataBase/ex1.xls', sheet_name='ex1')
def asd(products: pd.DataFrame) -> pd.DataFrame:
    products['low'] = products['low'].str.strip()
    products['recyclable'] = products['recyclable'].str.strip()
    return products[(products['low'] == 'Y') & (products['recyclable'] == 'Y')]

rec = asd(df)
print(rec)

