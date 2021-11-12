# -*- coding: utf-8 -*-
"""
Created on Thu Nov 11 20:46:53 2021

@author: rhyno
"""

# %% arithmetic

first_num = 7
second_num = 3

result_add = first_num + second_num

result_division = first_num / second_num

result_mult = first_num * second_num

result_subtract = first_num - second_num

result_remainder = first_num % second_num

result_divfloor = first_num // second_num

reconstruct = second_num * result_divfloor + result_remainder

print(
    first_num,
    second_num,
    result_add,
    result_division,
    result_mult,
    result_subtract,
    result_remainder,
    result_divfloor,
    reconstruct,
)


# %% assignment ops
x = 3
x = x +4
x += 4


# %% comparison ops

first_num = 4
second_num = 5.2

print(first_num + 1.2 == second_num)


