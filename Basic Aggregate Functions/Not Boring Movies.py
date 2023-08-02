import pandas as pd

def not_boring_movies(cinema :pd.DataFrame):
    cinema['id'] = cinema['id'].astype(int)
    cinema = cinema[(cinema['description'] != 'boring') & (cinema['id']%2 != 0)]
    return  cinema

df = pd.DataFrame([['1', 'War', 'great 3D', '8.9'],
                        ['2', 'Science', 'fiction', '8.5'],
                        ['3', 'irish', 'boring', '6.2'],
                        ['4', 'Ice song', 'Fantacy', '8.6'],
                        ['5', 'House card', 'Interesting', '9.1']],
                      columns=['id', 'movie', 'description', 'rating'])

print(not_boring_movies(df))