#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  1 23:56:39 2021

@author: rhyno466
"""

user_name = input('User Name: ')
user_age = int(input('User Age: '))

print('User is ' + user_name + 
      ' who is ' + str(user_age) + '\n')

int_1 = int(input('Enter an integer: '))
int_2 = int(input('Enter another integer: '))

print('The first input is: ', int_1, 
      '\nThe second input is: ',
      int_2, '\n\nThe sum is: ', int_1 + int_2)

lst = [1.2, 2.5, 3.5, 4.67]
lst_sum = sum(lst)
lst_len = len(lst)
lst_avg = lst_sum / lst_len

print('The average of the list is: ', lst_avg)

