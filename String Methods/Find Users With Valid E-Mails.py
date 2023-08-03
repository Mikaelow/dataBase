import pandas as pd

def valid_emails(users: pd.DataFrame) -> pd.DataFrame:
    chars = r'^[a-zA-Z][a-zA-Z0-9_.-]*\@leetcode\.com$'
    users = users[users['mail'].str.contains(chars)]
    return users

Users = pd.DataFrame([
['1', 'Winston', 'winston@leetcode.com'],
['2', 'Jonathan', 'jonathanisgreat'],
['3', 'Annabelle', 'bella-@leetcode.com'],
['4', 'Sally', 'sally.come@leetcode.com'],
['5', 'Marwan', 'quarz#2020@leetcode.com'],
['6', 'David', 'david69@gmail.com'],
['7', 'Shapiro', '.shapo@leetcode.com']
], 
columns=['user_id', 'name', 'mail']).astype({'user_id':'int64', 'name':'object', 'mail':'object'})

print(valid_emails(Users))