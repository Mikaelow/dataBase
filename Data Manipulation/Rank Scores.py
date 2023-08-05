import pandas as pd

def order_scores(scores: pd.DataFrame) -> pd.DataFrame:
    scores['rank'] = scores['score'].rank(method='dense',ascending=False)
    resoults = scores[['score','rank']]
    return resoults.sort_values(by='rank',ascending=True).reset_index(drop=True)


Scores = pd.DataFrame([
    ['1', '3.5'],
    ['2', '3.65'],
    ['3', '4.0'],
    ['4', '3.85'],
    ['5', '4.0'],
    ['6', '3.65']
], columns=['id', 'score']).astype({'id':'Int64', 'score':'Float64'})

print(order_scores(Scores))