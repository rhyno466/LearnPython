#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 23 20:49:26 2021

@author: rhyno466
"""
#%% poverty way
print("hello")
print("hello")
print("hello")
print("hello")
print("hello")
print("hello")
print("hello")
print("hello")
print("hello")
print("hello")

#%% For Loop
for i in range(100):
    print("Hello " + str(i))
# print('test')

#%% While Loop
i = 0
while i < 10:
    print("Hello " + str(i))
    i += 1

#%%
num_list = [3, 4, 5, 8, 12, -3, -7]
for number in num_list:
    print(number)
    if number < 0:
        print('Number is negative')
