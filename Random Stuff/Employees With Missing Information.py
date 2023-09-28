import pandas as pd

def find_employees(employees: pd.DataFrame, salaries: pd.DataFrame) -> pd.DataFrame:
    tbl_merged = pd.merge(employees,salaries,how='outer',on='employee_id')
    tbl_merged = tbl_merged[tbl_merged['name'].isnull() | tbl_merged['salary'].isnull()]
    tbl_merged = tbl_merged.drop(columns=['name','salary']).reset_index(drop=True)
    return tbl_merged.sort_values(by='employee_id')

data = [[2, 'Crew'], [4, 'Haven'], [5, 'Kristian']]
employees = pd.DataFrame(data, columns=['employee_id', 'name']).astype({'employee_id':'Int64', 'name':'object'})
data = [[5, 76071], [1, 22517], [4, 63539]]
salaries = pd.DataFrame(data, columns=['employee_id', 'salary']).astype({'employee_id':'Int64', 'salary':'Int64'})

if __name__ == '__main__':
    print(find_employees(employees,salaries))