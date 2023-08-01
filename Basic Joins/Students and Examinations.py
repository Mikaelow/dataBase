import pandas as pd

def students_and_examinations(students: pd.DataFrame, subjects: pd.DataFrame, examinations: pd.DataFrame) -> pd.DataFrame:
    merged_table = pd.merge(students, subjects, how = 'cross')
    examinations = examinations.groupby(['student_id', 'subject_name']).size().reset_index()
    merged_table = pd.merge(merged_table, examinations, on = ['student_id', 'subject_name'], how = 'left').fillna(0)
    merged_table.columns = ['student_id','student_name','subject_name','attended_exams']
    merged_table.sort_values(by=['student_id', 'subject_name'], ascending=[True, True], inplace=True)
    return merged_table

Students = pd.DataFrame([
['1', 'Alice'],
['2', 'Bob'],
['13', 'John'],
['6', 'Alex']
], columns=['student_id', 'student_name'])
Subjects = pd.DataFrame([
['Math'],
['Physics'],
['Programming']
], columns=['subject_name'])
Examinations = pd.DataFrame([
['1', 'Math'],
['1', 'Physics'],
['1', 'Programming'],
['2', 'Programming'],
['1', 'Physics'],
['1', 'Math'],
['13', 'Math'],
['13', 'Programming'],
['13', 'Physics'],
['2', 'Math'],
['1', 'Math']
], columns=['student_id', 'subject_name'])


print(students_and_examinations(Students,Subjects,Examinations))