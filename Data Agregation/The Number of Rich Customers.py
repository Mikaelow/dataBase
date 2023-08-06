import pandas as pd

def count_rich_customers(store: pd.DataFrame) -> pd.DataFrame:
    store = store[store['amount']>500]
    uniq_store = store['customer_id'].unique()
    resoults = len(uniq_store)
    return pd.DataFrame([resoults],columns=['rich_count'])

Store = pd.DataFrame([
    ['6', '1', '549'],
    ['8', '1', '834'],
    ['4', '2', '394'],
    ['11', '3', '657'],
    ['13', '3', '257']
], columns=['bill_id', 'customer_id', 'amount']).astype(
    {'bill_id':'int64', 'customer_id':'int64', 'amount':'int64'})
print(count_rich_customers(Store))