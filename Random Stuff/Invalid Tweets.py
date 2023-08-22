# Write a solution to find the IDs of the invalid tweets. 
# The tweet is invalid if the number of characters used in the content of the tweet is strictly greater than 15.
# Return the result table in any order.
# The result format is in the following example.

import pandas as pd

def invalid_tweets(tweets: pd.DataFrame) -> pd.DataFrame:
    invalid_tweets = tweets[tweets['content'].str.len()>15]
    return invalid_tweets[['tweet_id']]


data = [[1, 'Vote for Biden'], [2, 'Let us make America great again!']]
Tweets = pd.DataFrame(data, columns=['tweet_id', 'content']).astype(
    {'tweet_id':'Int64', 'content':'object'})


print(invalid_tweets(Tweets))

