import pandas as pd

def replace_employee_id_with_the_unique_identifier(employees: pd.DataFrame, employee_uni: pd.DataFrame) -> pd.DataFrame:
    mergedd = pd.merge(employee_uni, employees,  on='id',how = 'right')
    return mergedd[['unique_id','name']]

Employees = pd.DataFrame( [['1', 'Alice'],
                             ['7', 'Bob'],
                             ['11', 'Meir'],
                             ['90', 'Winston'],
                             ['3', 'Jonathan']],
                 columns=['id', 'name'])
EmployeeUNI = pd.DataFrame([['3', '1'],
                            ['11', '2'],
                            ['90', '3']],
                 columns = ['id', 'unique_id'])

a = replace_employee_id_with_the_unique_identifier(Employees,EmployeeUNI)
print(a)