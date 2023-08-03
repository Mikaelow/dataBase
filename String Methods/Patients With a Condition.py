import pandas as pd

def find_patients(patients: pd.DataFrame) -> pd.DataFrame:
    formula = '^DIAB1| DIAB1'
    patients = patients[patients['conditions'].str.contains(formula)]
    return patients

Patients = pd.DataFrame([
    ['1', 'Daniel', 'YFEV COUGH'],
['2', 'Alice', ''],
['3', 'Bob', 'DIAB100 MYOP'],
['4', 'George', 'ACNE DIAB100'],
['5', 'Alain', 'DIAB201']
], 
columns=['patient_id', 'patient_name', 'conditions']).astype({'patient_id':'int64', 'patient_name':'object', 'conditions':'object'})

print(find_patients(Patients))