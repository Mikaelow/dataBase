import pandas as pd

def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:
    employees['salary'] = employees.apply(lambda row: 0 if row['name'][0] == 'M' or row['employee_id'] % 2 == 0 else row['salary'], axis=1)
    employees.columns = ['employee_id','name','bonus']
    sorted = employees[['employee_id','bonus']].sort_values(by = ['employee_id'])
    return sorted


Employees = pd.DataFrame([['2', 'Meir', '3000'],   
['3', 'Michael', '3800'],
['7', 'Addilyn', '7400'],
['8', 'Juan', '6100'],   
['9', 'Kannon', '7700']]
                         , columns=['employee_id', 'name', 'salary']).astype({'employee_id':'int64', 'name':'object', 'salary':'int64'})

print(calculate_special_bonus(Employees))