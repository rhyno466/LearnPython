#%%
import os
import pandas as pd
# %%
data_dir = os.path.join(os.getcwd(), 'data')
print(data_dir)
# %%
shots = pd.read_csv(os.path.join(data_dir, 'shots.csv'))
shots.head()
# %%
shots.columns
# %%
shots.shape
# %%
shots['name'].head()
# %%
type(shots['name'])
# %%
shots['name'].to_frame().head()
# %%
type(shots['name'].to_frame().head())
# %%
shot_cols = shots.columns.tolist()
# %%
shots[['name', 'pos', 'hand', 'goal']].head()
# %%
shots.set_index('shot_id').head()
# %%
shots.head()
# %%
shots.set_index('shot_id', inplace=True)
# %%
shots.head()
# %%
shots = pd.read_csv(os.path.join(data_dir, 'shots.csv'))
# %%
shots.head()
# %%
shots = shots.set_index('shot_id')
# %%
shots.head()
# %%
shots_ot = shots.loc[shots['period_type'] == 'OVERTIME', \
    ['name', 'period', 'hand', 'goal']]
# %%
shots_ot.head()
# %%
shots_ot.sort_values('name', inplace=True)
# %%
shots_ot.head()
# %%
shots_ot['pos'] =  shots['pos']
# %%
shots_ot.head()
# %%
# TEST INDEX EQUALS
#%%
shots_ot.to_csv(os.path.join(data_dir, 'shots_ot.csv'))
# %%
shots_ot.to_csv(os.path.join(data_dir, 'shots_ot_no_index.csv'),\
    index=False)

# %%
