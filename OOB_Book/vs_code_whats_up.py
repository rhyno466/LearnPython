# from arepl_dump import dump

#%%
from typing_extensions import Self


a = 12

ryne = True

if ryne:
    print('Fuck')
else:
    print('timma')
    
x = 12

hits = ['ryne', 'allison', 'allison', 'timma', 'jimmy']

for h in hits:
    print(h)
    
for i in range(0,x):
    print(i)


    
# %%

class robot:
    def __init__(self, name, age):
        self.name = name
        self.age = age
     
    def say_name(self):
        print(f'my name is {self.name}')
        
    def say_age(self):
        print(f'my age is {self.age}')
        
# %%
ryne = robot('Ryne', 34)

ryne.say_age()
ryne.say_name()