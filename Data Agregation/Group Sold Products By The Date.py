import pandas as pd

def categorize_products(activities: pd.DataFrame) -> pd.DataFrame:
    activities.drop_duplicates(inplace=True)
    grouped_activities = activities.groupby('sell_date')['product'].count().reset_index()
    grouped_activities = grouped_activities.rename(columns = {'product':'num_sold'})
    name_activities = activities.sort_values(by = 'product'
                                             ,ascending=True ).groupby('sell_date')['product'].apply(
        lambda x: ','.join(x)
        ).reset_index()
    tbl_merged = pd.merge(grouped_activities,name_activities,how='inner',on='sell_date')
    tbl_merged = tbl_merged.sort_values(by = 'sell_date',ascending=True)
    tbl_merged.rename(columns={'product':'products'},inplace=True)
    return tbl_merged


data = [['2020-05-30', 'Headphone'], ['2020-06-01', 'Pencil'], 
        ['2020-06-02', 'Mask'], ['2020-05-30', 'Basketball'], 
        ['2020-06-01', 'Bible'], ['2020-06-02', 'Mask'], 
        ['2020-05-30', 'T-Shirt']]
Activities = pd.DataFrame(data, columns=['sell_date', 'product']).astype(
    {'sell_date':'datetime64[ns]', 'product':'object'})

print(categorize_products(Activities))