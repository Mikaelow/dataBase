# Write a solution to report the movies with an odd-numbered ID and a description that is not "boring".
# Return the result table ordered by rating in descending order.
# The result format is in the following example.

import pandas as pd

def not_boring_movies(cinema: pd.DataFrame) -> pd.DataFrame:
    return cinema[(cinema['id']%2 != 0) & (cinema['description'] != 'boring')].sort_values(by='rating', ascending=False)


data = [[1, 'War', 'great 3D', 8.9], [2, 'Science', 'fiction', 8.5], [3, 'irish', 'boring', 6.2], 
        [4, 'Ice song', 'Fantacy', 8.6], [5, 'House card', 'Interesting', 9.1]]
Cinema = pd.DataFrame(data, columns=['id', 'movie', 'description', 'rating']).astype(
    {'id':'Int64', 'movie':'object', 'description':'object', 'rating':'Float64'})


if  __name__ == '__main__':
    print(not_boring_movies(Cinema))