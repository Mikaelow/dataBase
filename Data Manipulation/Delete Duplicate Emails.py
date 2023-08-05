import pandas as pd

def delete_duplicate_emails(person: pd.DataFrame) -> None:
    person.sort_values(by = 'id',inplace=True)
    person.reset_index(drop=True,inplace=True)
    person.drop_duplicates(subset='email',keep='first',inplace=True)

Person = pd.DataFrame([
    ['3', 'john@example.com'],
    ['2', 'bob@example.com'],
    ['1', 'john@example.com']
    ],columns=['id','email']).astype({'id':'int64', 'email':'object'})
delete_duplicate_emails(Person)
print(Person)