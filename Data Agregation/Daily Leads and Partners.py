import pandas as pd

def daily_leads_and_partners(daily_sales: pd.DataFrame):
    result = daily_sales.groupby(['make_name', 'date_id']).agg(
    unique_leads=('lead_id', 'nunique'),
    unique_partners=('partner_id', 'nunique')
).reset_index()
    return result
data = [['2020-12-8', 'toyota', 0, 1],
        ['2020-12-8', 'toyota', 1, 0],
        ['2020-12-8', 'toyota', 1, 2],
        ['2020-12-7', 'toyota', 0, 2],
        ['2020-12-7', 'toyota', 0, 1],
        ['2020-12-8', 'honda', 1, 2],
        ['2020-12-8', 'honda', 2, 1],
        ['2020-12-7', 'honda', 0, 1],
        ['2020-12-7', 'honda', 1, 2],
        ['2020-12-7', 'honda', 2, 1]]
DailySales = pd.DataFrame(data, columns=['date_id', 'make_name', 'lead_id', 'partner_id']).astype(
    {'date_id':'datetime64[ns]', 'make_name':'object', 'lead_id':'Int64', 'partner_id':'Int64'})

print(daily_leads_and_partners(DailySales))