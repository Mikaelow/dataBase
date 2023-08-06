import pandas as pd

def count_salary_categories(accounts: pd.DataFrame):
    Low_Salary = len(accounts[accounts['income']<20000])
    Average_Salary = len(accounts[(accounts['income']>=20000) & (accounts['income']<=50000)])
    High_Salary = len(accounts[accounts['income']>50000])
    data = [('High Salary', High_Salary),
            ('Low Salary', Low_Salary),
            ('Average Salary', Average_Salary)]
    amout_salary = pd.DataFrame(data, columns=['category', 'accounts_count'])
    return amout_salary



Accounts = pd.DataFrame([
    ['3', '108939'],
    ['2', '12747'],
    ['8', '87709'],
    ['6', '91796']
], columns=['account_id', 'income']).astype(
    {'account_id':'Int64', 'income':'Int64'})
print(count_salary_categories(Accounts))