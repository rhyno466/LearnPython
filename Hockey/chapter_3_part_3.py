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
