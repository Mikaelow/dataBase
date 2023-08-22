# Write a solution to find all the authors that viewed at least one of their own articles.
# Return the result table sorted by id in ascending order.
# The result format is in the following example.


import pandas as pd
from pprint import pprint 

def article_views(views: pd.DataFrame) -> pd.DataFrame:
    showRecords = views[views['author_id'] == views['viewer_id']]
    resoults = showRecords.drop_duplicates()
    sort = resoults.sort_values(by = 'author_id')
    sort.rename(columns={'author_id':'id'}, inplace=True)
    cos = sort[['id']].drop_duplicates()
    return cos

data = [[1, 3, 5, '2019-08-01'], [1, 3, 6, '2019-08-02'], [2, 7, 7, '2019-08-01'], 
        [2, 7, 6, '2019-08-02'], [4, 7, 1, '2019-07-22'], [3, 4, 4, '2019-07-21'], [3, 4, 4, '2019-07-21']]
Views = pd.DataFrame(data, columns=['article_id', 'author_id', 'viewer_id', 'view_date']).astype(
    {'article_id':'Int64', 'author_id':'Int64', 'viewer_id':'Int64', 'view_date':'datetime64[ns]'})


if __name__ == '__main__':
    pprint(article_views(Views))