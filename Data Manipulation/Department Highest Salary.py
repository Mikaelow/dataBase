import pandas as pd

def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    employee['desne_rank'] = employee.groupby('departmentId')['salary'].rank(method='dense',ascending=False)
    employee =  employee[employee['desne_rank'] == 1]
    merged_table = pd.merge(employee,department, left_on='departmentId', right_on='id', how='left')
    result = merged_table[['name_y', 'name_x', 'salary']]  
    result.columns = ['Department', 'Employee', 'Salary'] 
    return result
    



Employee = pd.DataFrame([
['1', 'Joe', '70000', '1'],  
['2', 'Jim', '90000', '1'],  
['3', 'Henry', '80000', '2'],
['4', 'Sam', '60000', '2'],  
['5', 'Max', '90000', '1']  
], columns=['id', 'name', 'salary', 'departmentId']).astype({'id':'Int64', 'name':'object', 'salary':'Int64', 'departmentId':'Int64'})
Department = pd.DataFrame([
['1', 'IT'],
['2', 'Sales']
], columns=['id', 'name']).astype({'id':'Int64', 'name':'object'})


print(department_highest_salary(Employee,Department))