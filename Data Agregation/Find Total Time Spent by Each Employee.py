import pandas as pd

def total_time(employees: pd.DataFrame) -> pd.DataFrame:
    employees['total_time'] = employees.apply(lambda row: row['out_time']-row['in_time'],axis=1)
    sortowanie = employees.groupby(['event_day','emp_id'])['total_time'].sum().reset_index()
    sortowanie.rename(columns={'event_day':'day'},inplace=True)
    return sortowanie.sort_values(by='total_time',ascending=False)

Employees = pd.DataFrame([
    ['1', '2020-11-28', '4', '32'],
    ['1', '2020-11-28', '55', '200'],
    ['1', '2020-12-3', '1', '42'],
    ['2', '2020-11-28', '3', '33'],
    ['2', '2020-12-9', '47', '74']
], columns=['emp_id', 'event_day', 'in_time', 'out_time']).astype(
    {'emp_id':'Int64', 'event_day':'datetime64[ns]', 'in_time':'Int64', 'out_time':'Int64'})

print(total_time(Employees))