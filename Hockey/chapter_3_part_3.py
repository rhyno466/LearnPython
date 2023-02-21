#%%
import os
import pandas as pd
# %%
data_dir = os.path.join(os.getcwd(), 'data')
print(data_dir)
#%%
pg = pd.read_csv(os.path.join(data_dir,'player_games.csv'))

#%%
pg.mean()
# %%
pg.max()
# %%
pg[['shots', 'goals', 'assists','hits']].mean(axis=0)
# %%
pg[['shots', 'goals', 'assists','hits']].mean(axis=1).head()

# %%
pg['defender_score'] = (pg['pos'] == 'D') & (pg['goals'] > 0)
pg[['defender_score', 'name', 'goals']].sample(5)
pg['defender_score'].mean()
# %%
pg['defender_score'].sum()
# %%
(pg['pen_min'] > 20).any()
# %%
(pg['time_ice'] > 0).all()
# %%
(pg[['goals', 'assists']] > 2).any(axis=1)
# %%
(pg[['goals', 'assists']] > 2).any(axis=1).sum()
# %%
(pg[['time_ice_sh', 'time_ice_pp']] == 0).all(axis=1).sum()
# %%
pg['pos'].value_counts()
# %%
pg['pos'].value_counts(normalize=True,)
# %%
pd.crosstab(pg['team'], pg['pos']).sample(5)
# %%
