# Reformat the table such that there is a department id column and a revenue column for each month.
# Return the result table in any order.
# The result format is in the following example. 

import pandas as pd

def reformat_department_table(department : pd.DataFrame):
    id
    new_tbl = pd.DataFrame({'id':department['id']})
    return new_tbl



data = [[1, 8000, 'Jan'], [2, 9000, 'Jan'], [3, 10000, 'Feb'], [1, 7000, 'Feb'], [1, 6000, 'Mar']]
Department = pd.DataFrame(data, columns=['id', 'revenue', 'month']).astype(
    {'id':'Int64', 'revenue':'Int64', 'month':'object'})


if(__name__ == '__main__'):
    print(reformat_department_table(Department))