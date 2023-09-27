import pandas as pd

def capital_gainloss(stocks: pd.DataFrame) -> pd.DataFrame:
    stocks = stocks.groupby(['stock_name','operation']).sum().reset_index()
    stock_selled = stocks[stocks['operation'] =='Sell'].reset_index().drop('index',axis=True)
    stock_buyed = stocks[stocks['operation'] =='Buy'].reset_index().drop('index',axis=True)
    stock_merged = pd.merge(stock_selled,stock_buyed,how = 'outer', on='stock_name')
    stock_merged.fillna(0,inplace=True)
    stock_merged['capital_gain_loss'] = stock_merged['price_x'] - stock_merged['price_y'] 
    return stock_merged[['stock_name','capital_gain_loss']]

data = [ ['Corona Masks', 'Buy', 2, 10], ['Leetcode', 'Sell', 5, 9000], ['Handbags', 'Buy', 17, 30000], ['Corona Masks', 'Sell', 3, 1010], ['Corona Masks', 'Buy', 4, 1000], ['Corona Masks', 'Sell', 5, 500], ['Corona Masks', 'Buy', 6, 1000], ['Handbags', 'Sell', 29, 7000], ['Corona Masks', 'Sell', 10, 10000]]
stocks = pd.DataFrame(data, columns=['stock_name', 'operation', 'operation_day', 'price']).astype({'stock_name':'object', 'operation':'object', 'operation_day':'Int64', 'price':'Int64'})
print(capital_gainloss(stocks))