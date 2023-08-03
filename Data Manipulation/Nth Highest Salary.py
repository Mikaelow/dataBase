import pandas as pd
import numpy as np

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    if N<=len(employee):
        sorted_employee = employee.sort_values(by='salary', ascending=False).reset_index(drop=True)
        nth_row  = sorted_employee.loc[N-1,'salary']
        return pd.DataFrame([nth_row],columns=[f'getNthHighestSalary({N})'])
    else:
        return pd.DataFrame([np.NaN],columns = [f'getNthHighestSalary({N})'])



Emoloyee = pd.DataFrame([
    ['1', '100'],
    ['2', '200'],
    ['3', '300']
],
columns= ['id', 'salary']).astype({'id':'int64','salary':'int64'})
print(nth_highest_salary(Emoloyee,30))