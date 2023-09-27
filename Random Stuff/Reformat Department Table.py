import pandas as pd

def reformat_table(department: pd.DataFrame) -> pd.DataFrame:
    new_tbl = pd.DataFrame(columns=['id','Jan_Revenue','Feb_Revenue','Mar_Revenue','Apr_Revenue','May_Revenue','Jun_Revenue','Jul_Revenue','Aug_Revenue','Sep_Revenue','Oct_Revenue','Nov_Revenue','Dec_Revenue'])
    new_tbl['id'] = department['id']
    new_tbl.drop_duplicates(inplace=True)
    for index, row in department.iterrows():
        new_tbl.loc[new_tbl['id'] == row['id'], row['month']+'_Revenue'] = row['revenue']
    return new_tbl
     

data = [[1, 8000, 'Jan'], [2, 9000, 'Jan'], [3, 10000, 'Feb'], [1, 7000, 'Feb'], [1, 6000, 'Mar']]
department = pd.DataFrame(data, columns=['id', 'revenue', 'month']).astype({'id':'Int64', 'revenue':'Int64', 'month':'object'})


if(__name__ == '__main__'):
    print(reformat_department_table(department))