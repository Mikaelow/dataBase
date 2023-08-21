import pandas as pd

def duplicate_emails(person: pd.DataFrame) -> pd.DataFrame:
    couted_emails = person.groupby('email').agg(counted = ('email','count')).reset_index()
    duplicated_email = couted_emails[couted_emails['counted']>1]
    return duplicated_email[['email']]




data = [[1, 'a@b.com'], [2, 'c@d.com'], [3, 'a@b.com']]
Person = pd.DataFrame(data, columns=['id', 'email']).astype(
    {'id':'Int64', 'email':'object'})

if __name__ == '__main__':
    print(duplicate_emails(Person))