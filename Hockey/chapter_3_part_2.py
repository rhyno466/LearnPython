#%%
import os
import pandas as pd
# %%
data_dir = os.path.join(os.getcwd(), 'data')
print(data_dir)
#%%
pg = pd.read_csv(os.path.join(data_dir,'player_games.csv'))
# %%
pg['penalty_time'] = 2
pg[['name', 'shots', 'goals', 'penalty_time']].head()
# %%
pg['penalty_time'] = 5
pg[['name', 'shots', 'goals', 'penalty_time']].head()

# %%
print(pg.columns.to_list())
pg['net_penalty_min'] = (pg['time_ice_pp'] - pg['time_ice_sh'])
pg[['name', 'game_id', 'net_penalty_min']].head()
# %%
import numpy as np
pg['biggest_impact'] = np.abs(pg['plus_minus'])
pg['ln_min'] = np.log(pg['time_ice'])
# %%
pg['rink_width'] = 85
# %%
pg[['name', 'game_id', 'rink_width']].sample(5)
# %%
pg['name'].str.upper().sample(5)
# %%
pg['name'].str.replace('. ', '-').sample(5)
# %%
(pg['name'] + ', ' + pg['pos'] + ' - ' + pg['team']).sample(5)
# %%
pg['name'].str.replace('.', '').str.lower().sample(5)
# %%
pg['is_defender'] = pg['pos'] == 'D'
# %%
pg[['name', 'is_defender', 'pos']].sample(5)
# %%
pg['is_a_w'] = (pg['pos'] == 'LW') | (pg['pos'] == 'RW')
pg[['name', 'pos', 'is_a_w']].sample(5)
# %%
pg['balanced_off'] = (pg['goals'] > 0) & (pg['assists'] > 0)
pg[['name', 'goals', 'assists', 'balanced_off']].sample(5)
# %%
pg['is_not_a_w'] = ~(pg['pos'] == 'LW') | (pg['pos'] == 'RW')
pg[['name', 'pos', 'is_a_w', 'is_not_a_w']].sample(5)

# %%
(pg[['goals', 'assists']] > 0).sample(5)
# %%
def is_e_metro(team):
    return team in ['WSH', 'NYI', 'PIT', 'CAR', 'CBJ', 'NYR', 'NJD']
# %%
pg['is_e_metro'] = pg['team'].apply(is_e_metro)
pg[['team', 'is_e_metro']].sample(5)
# %%
pg['is_e_metro_alt'] = pg['team'].apply(lambda x: x in  ['WSH', 'NYI', 'PIT', 'CAR', 'CBJ', 'NYR', 'NJD'])
pg[['team', 'is_e_metro', 'is_e_metro_alt']].sample(5)
# %%
pg.drop('is_skill_alternate', axis=1, inplace=True)
# %%
pg.columns = [x.upper() for x in pg.columns]
pg.head()
# %%
pg.columns = [x.lower() for x in pg.columns]
pg.head()
# %%
pg.rename(columns={'fo': 'faceoffs'}, inplace=True)
# %%
pg['shot_pct'] = pg['goals'] / pg['shots']
pg[['name', 'team', 'goals', 'shots', 'shot_pct']].sample(5)
# %%
pg['shot_pct'].isnull().head(10)
pg['shot_pct'].notnull().head(10)
# %%
pg['shot_pct'].fillna(-99).head(10)
# %%
pg['month'] = pg['date'].astype(str).str[4:6]
pg[['name', 'game_id', 'date', 'month']]
# %%
pg['month'].astype(int)
# %%
pg.dtypes
# %%
