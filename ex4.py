import pandas as pd

view = pd.DataFrame([['1', '3', '5', '2019-08-01'],
    ['1', '3', '6', '2019-08-02'],
    ['2', '7', '7', '2019-08-01'],
    ['2', '7', '6', '2019-08-02'],
    ['4', '7', '1', '2019-07-22'],
    ['3', '4', '4', '2019-07-21'],
    ['3', '4', '4', '2019-07-21']], columns=['article_id', 'author_id', 'viewer_id', 'view_date'])
def article_views_i(views: pd.DataFrame) -> pd.DataFrame:
        showRecords = views[views['author_id'] == views['viewer_id']]
        resoults = showRecords.drop_duplicates()
        sort = resoults.sort_values(by='author_id')
        sort.rename(columns={'author_id': 'id'}, inplace=True)
        return sort[['id']]

a = article_views_i(view)
print(a)
