#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  6 15:52:13 2021

@author: rhyno466
"""

print('Welcome to the program!')
msg = input('Enter a message: ')
ltr = input('Enter a letter: ')


#%%
num = msg.count(ltr)

pct = round(num / len(msg.replace(' ', '')) * 100, 2)

#%%
print(f'{ltr} occurs {num} times in the provided message, which is {pct}% of the letters in the message!!')


#%% SOLUTION


print('Welcome to the program!')
msg = input('Enter a message: ')
ltr = input('Enter a letter: ')

msg_up = msg.upper()
ltr_up = ltr.upper()

num = msg_up.count(ltr_up)

pct = round(num / len(msg_up.replace(' ', '')) * 100, 2)

print(f'{ltr} occurs {num} times in the provided message, which is {pct}% of the letters in the message!!')
