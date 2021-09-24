#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 23 21:08:23 2021

@author: rhyno466
"""


def list_max(lst):
    return max(lst)


#%%


def list_max_dumb(lst):
    maxval = 0
    for i in lst:
        if i > maxval:
            maxval = i

    return maxval


#%%
my_list = [1, 3, 12, 9.9]
print(list_max(my_list))
print(list_max_dumb(my_list))

#%%
nums = []

for i in range(5):
    nums.append(float(input("num: ")))
    if len(nums) == 5:
        print(sum(nums) / len(nums))

#%%

mums = []

k = True

while k:
    inp = float(input("num? "))
    if inp == 0:
        k = False
    else:
        mums.append(inp)

print(sum(mums) / len(mums))





