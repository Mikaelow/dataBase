#Write a solution to find the employees who earn more than their managers.
#Return the result table in any order.
#The result format is in the following example. 

import pandas as pd

def find_employees(employee: pd.DataFrame)  -> pd.DataFrame:
    merged_table = pd.merge(employee, employee, right_on ='id', left_on ='managerId',how = 'inner')
    higher_salary = merged_table[merged_table['salary_x']>merged_table['salary_y']]
    higher_salary = higher_salary.rename(columns={'name_x':'Employee'})
    return higher_salary[['Employee']]

data = [[1, 'Joe', 70000, 3], [2, 'Henry', 80000, 4], [3, 'Sam', 60000, None], [4, 'Max', 90000, None]]
Employee = pd.DataFrame(data, columns=['id', 'name', 'salary', 'managerId']).astype(
    {'id':'Int64', 'name':'object', 'salary':'Int64', 'managerId':'Int64'})
print(find_employees(Employee))