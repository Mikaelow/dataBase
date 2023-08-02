from datetime import date

import pandas as pd

def average_selling_price(prices : pd.DataFrame, units_sold : pd.DataFrame):
    prices['start_date'] = prices['start_date'].astype(date)
    prices['end_date'] = prices['end_date'].astype(date)
    units_sold['purchase_date'] = units_sold['purchase_date'].astype(date)

    merge = pd.merge(prices, units_sold, on=(
        prices['product_id'] == units_sold['product_id'] & units_sold['purchase_date']
    ), how = 'left')

Prices = pd.DataFrame([['1', '2019-02-17', '2019-02-28', '5'],
                        ['1', '2019-03-01', '2019-03-22', '20'],
                        ['2', '2019-02-01', '2019-02-20', '15'],
                        ['2', '2019-02-21', '2019-03-31', '30']],
                        columns=['product_id','start_date','end_date','price'])
UnitsSold = pd.DataFrame([['1', '2019-02-25', '100'],
                        ['1', '2019-03-01', '15'],
                        ['2', '2019-02-10', '200'],
                        ['2', '2019-03-22', '30']],
                        columns=['product_id','purchase_date','units'])
