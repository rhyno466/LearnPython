# -*- coding: utf-8 -*-
"""
Created on Sat Sep 25 16:19:27 2021

@author: rhyno
"""
import my_comps

#%%
nums = []
with open("various_nums", "r") as f:
    for line in f:
        nums.append(float(line))

print(my_comps.list_max(nums))

#%%
cities = []
with open("unordered_cities.txt", "r") as g:
    for line in g:
        cities.append(line.rstrip('\n'))
city_list_sorted = sorted(cities)
print(city_list_sorted)

with open('ordered_cities.txt', 'w') as h:
    for city in city_list_sorted:
        h.write(city + '\n')
        
print('Done')