# Write a solution to find managers with at least five direct reports.
# Return the result table in any order.
# The result format is in the following example.

import pandas as pd

def find_managers(employee: pd.DataFrame) -> pd.DataFrame:
    counted = employee.groupby('managerId').agg(
        policzone=('managerId', 'count')
    ).reset_index()
    counted = counted[counted['policzone'] >= 5]
    merged_table = pd.merge(counted, employee, how='left', left_on='managerId', right_on='id')
    if merged_table['name'].isna().all():
        return pd.DataFrame(columns=['name'])
    return merged_table[['name']]



data = [[101, 'John', 'A', None], 
        [102, 'Dan', 'A', 100], 
        [103, 'James', 'A', 100], 
        [104, 'Amy', 'A', 100], 
        [105, 'Anne', 'A', 100], 
        [106, 'Ron', 'B', 100]]
Employee = pd.DataFrame(data, columns=['id', 'name', 'department', 'managerId']).astype(
    {'id':'Int64', 'name':'object', 'department':'object', 'managerId':'Int64'})

print(find_managers(Employee))