import pandas as pd
def students_and_examinations(students: pd.DataFrame, subjects: pd.DataFrame, examinations: pd.DataFrame) -> pd.DataFrame:
    merged_table = pd.merge(students, subjects, how = 'cross')
    examinations = examinations.groupby(['student_id', 'subject_name']).size().reset_index()
    merged_table = pd.merge(merged_table, examinations, on = ['student_id', 'subject_name'], how = 'left').fillna(0)
    merged_table.columns = ['student_id','student_name','subject_name','attended_exams']
    merged_table.sort_values(by=['student_id', 'subject_name'], ascending=[True, True], inplace=True)
    return merged_table

data = [[1, 'Alice'], [2, 'Bob'], [13, 'John'], [6, 'Alex']]
Students = pd.DataFrame(data, columns=['student_id', 'student_name']).astype({'student_id':'Int64', 'student_name':'object'})
data = [['Math'], ['Physics'], ['Programming']]
Subjects = pd.DataFrame(data, columns=['subject_name']).astype({'subject_name':'object'})
data = [[1, 'Math'], [1, 'Physics'], [1, 'Programming'], [2, 'Programming'], [1, 'Physics'], [1, 'Math'], [13, 'Math'], [13, 'Programming'], [13, 'Physics'], [2, 'Math'], [1, 'Math']]
Examinations = pd.DataFrame(data, columns=['student_id', 'subject_name']).astype({'student_id':'Int64', 'subject_name':'object'})

print(students_and_examinations(Students,Subjects,Examinations))