import pandas as pd

def actors_and_directors(actor_director: pd.DataFrame) -> pd.DataFrame:
    counted_actors = actor_director.groupby(['actor_id','director_id']).count().reset_index()
    resoults = counted_actors[counted_actors['timestamp']>=3]
    return resoults[['actor_id','director_id']]



data = [[1, 1, 0], 
        [1, 1, 1], 
        [1, 1, 2], 
        [1, 2, 3], 
        [1, 2, 4], 
        [2, 1, 5], 
        [2, 1, 6]]
ActorDirector = pd.DataFrame(data, columns=['actor_id', 'director_id', 'timestamp']).astype(
    {'actor_id':'int64', 'director_id':'int64', 'timestamp':'int64'})


print(actors_and_directors(ActorDirector))