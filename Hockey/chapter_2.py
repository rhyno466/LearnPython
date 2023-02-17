#%%
1 + 1
# %%
print(1 + 1)
# %%
goals_scored = 2
# %%
goals_scored += 1
# %%
penalty_minutes = 15
print(type(penalty_minutes))
puck_speed = 82.5
print(type(puck_speed))
starting_lw = 'David Perron'
startint_c = 'Dylan Larkin'
print(type(starting_lw), type(startint_c))
# %%
starters = f'{starting_lw}, {startint_c}, ect'
print(starters)
# %%
miracle = 'Do you believe in miracles?'
print(miracle.upper())
# %%
'Bernie Gefferion'.replace('Bernie', 'Boom Boom')

# %%
foo = 'sid'.capitalize()
# %%
team1_goals = 2
team2_goals = 1
# %%
team1_win = team1_goals > team2_goals
team2_win = team2_goals > team1_goals
teams_tied = team1_goals == team2_goals
teams_not_tied = team1_goals != team2_goals
# %%
teams_not_tied
# %%
shootout = (team1_goals > 4) and (team2_goals > 4)
atleast_one_good_team = (team1_goals > 4) or (team2_goals > 3)
you_guys_bad = not ((team1_goals > 1) or (team2_goals > 1))
meh = not (shootout or atleast_one_good_team or you_guys_bad)
# %%
if team1_win:
    message = 'Nice win 1!'
elif team2_win:
    message = 'Nice win 2!'
else:
    message = 'Tie'
print(message)
# %%
first_line = ['ovi', 'sid', 'bert']
# %%
first_line[0]
# %%
first_line[0:2]
# %%
first_line[-2]
# %%
first_line[-2:]
# %%
first_line_dict = {'lw': 'ovi',
                   'c': 'sid',
                   'rw': 'bert'}
# %%
first_line_dict['lw']
# %%
first_line_dict['rd'] = 'mo'
# %%
first_line_dict
# %%
lw, rw = ['ovi', 'sid']
# %%
lw
# %%
first_line_upper = []
for player in first_line:
    first_line_upper.append(player.upper())
# %%
for x in first_line_dict:
    print(f'Position: {x}')
# %%
for x in first_line_dict:
  print(f'Position: {x}')
  print(f'Player: {first_line_dict[x]}') 
# %%
for x, y in first_line_dict.items():
    print(f'Position: {x}')
    print(f'Player: {y}') 
    
# %%
first_line_proper = [x.title() for x in first_line]
print(first_line_proper)
# %%
[x.title() for x in first_line[0:2]]
# %%
[x for x in first_line if x.startswith('b')]
# %%
salary_per_player = {'dylan larkin': 9000000,
                     'tyler bertuzzi': 4500000,
                     'moritz seider': 6450000}
# %%
salary_m_per_player_upper = {name.upper(): \
    salary/1000000 for name, salary in \
        salary_per_player.items()}
# %%
sum({salary for _, salary in salary_m_per_player_upper.items()})
# %%
def team_points(wins:int, losses:int, ot_losses:int=0) -> int:
    return 2 * wins + ot_losses
# %%
def do_to_list(lst:list, fn, desc:str) -> str:
    val = fn(lst)
    return f'{desc}: {val}'
# %%
def last_elem(lst:list):
    return lst[-1]
# %%
do_to_list([2,3,4,5,6], last_elem, 'Last Elem')

# %%
do_to_list([1,2,3], lambda x: sum(x) + 1, 'Lambda')
# %%
import os
# %%
os.cpu_count()
# %%
base = os.getcwd()
os.path.join(base, 'data')
# %%base = os.getcwd()
os.path.join(base, 'data', 'shots.csv')
# %%
