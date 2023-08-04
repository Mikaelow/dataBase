import pandas as pd
import numpy as np

def second_highest_salary(employee: pd.DataFrame):
    unique_values = employee.salary.unique() #zmienia w liste
    if len(unique_values)>=2:  
        sorted_values = sorted(unique_values,reverse=True)[1]
        return pd.DataFrame([sorted_values],columns=['SecondHighestSalary'])
    else: 
        return pd.DataFrame([np.NaN],columns = ['SecondHighestSalary'])

Emoloyee = pd.DataFrame([
    ['1', '100'],
    ['2', '200'],
    ['3', '300'],

],
columns= ['id', 'salary']).astype({'id':'int64','salary':'int64'})
print(second_highest_salary(Emoloyee))