import pandas as pd

def count_unique_subjects(teacher: pd.DataFrame) -> pd.DataFrame:
    teacher['ranking'] = teacher.groupby('teacher_id')['subject_id'].rank(method='dense',ascending=True)
    no_duplicate = teacher.drop_duplicates(['ranking','teacher_id'])
    del teacher
    counted_records = no_duplicate.groupby('teacher_id')['subject_id'].count().reset_index()
    del no_duplicate
    counted_records.rename(columns={'subject_id':'cnt'},inplace=True)
    return counted_records


data = [[1, 2, 3], [1, 2, 4], [1, 3, 3], [2, 1, 1], [2, 2, 1], [2, 3, 1], [2, 4, 1]]
Teacher = pd.DataFrame(data, columns=['teacher_id', 'subject_id', 'dept_id']).astype(
    {'teacher_id':'Int64', 'subject_id':'Int64', 'dept_id':'Int64'})

print(count_unique_subjects(Teacher))