import pandas as pd

def fix_names(users: pd.DataFrame) -> pd.DataFrame:
    users['name'] = users['name'].apply(lambda names:names[0].upper()+names[1:].lower())
    return users.sort_values(by = 'user_id')




Users = pd.DataFrame([['1', 'aLice'],
                    ['2', 'bOB']], 
                    columns=['user_id', 'name']).astype({'user_id':'Int64', 'name':'object'})

print(fix_names(Users))