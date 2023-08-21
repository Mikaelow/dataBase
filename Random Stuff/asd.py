import pandas as pd

def combine_two_tables(person: pd.DataFrame, address: pd.DataFrame) -> pd.DataFrame:
    merged_table = pd.merge(person, address, on = 'personId',how = 'left')
    #return merged_table[['firstName','lastName','city','state']]
    return person

data = [[1, 'Wang', 'Allen'], [2, 'Alice', 'Bob']]
Person = pd.DataFrame(data, columns=['personId', 'firstName', 'lastName']).astype(
    {'personId':'Int64', 'firstName':'object', 'lastName':'object'})
data = [[1, 2, 'New York City', 'New York'], [2, 3, 'Leetcode', 'California']]
Address = pd.DataFrame(data, columns=['addressId', 'personId', 'city', 'state']).astype(
    {'addressId':'Int64', 'personId':'Int64', 'city':'object', 'state':'object'})

print(combine_two_tables(Person, Address))