import pandas as pd

def find_classes(courses: pd.DataFrame) -> pd.DataFrame:
    courses = courses.groupby('class')['student'].count().reset_index()
    courses = courses.rename(columns={'student':'policzone'})
    resoults = courses[courses['policzone']>=5]
    return resoults[['class']]


data = [['A', 'Math'], ['B', 'English'], ['C', 'Math'], ['D', 'Biology'], ['E', 'Math'], ['F', 'Computer'], ['G', 'Math'], ['H', 'Math'], ['I', 'Math']]
Courses = pd.DataFrame(data, columns=['student', 'class']).astype({'student':'object', 'class':'object'})
print(find_classes(Courses))