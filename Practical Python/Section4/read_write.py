# -*- coding: utf-8 -*-
"""
Created on Sat Sep 25 15:46:39 2021

@author: rhyno
"""
# import os
# from os import remove
# from os.path import exists
import my_comps

#%%

# with open("C:/Users/rhyno/OneDrive/Documents/GitHub/LearnPython/Practical Python/Section4/file_test", "r") as f:
#     # print(f.read())
#     for line in f:
#         print(line.rstrip("\n"))

#%%
# with open("new_file", "a+") as f:
#     f.write("test 123\n")

#%%
# filenname = "new_file"

# if exists("new_file"):
#     remove("new_file")

#%%
num1 = int(input('Num 1: '))
num2 = int(input('Num 2: '))

print(str(num1) + ' + ' + str(num2) + ' = ' + str(my_comps.add_2_nums(num1, num2)))