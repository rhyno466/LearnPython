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
