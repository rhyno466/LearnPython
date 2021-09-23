# -*- coding: utf-8 -*-
"""
Created on Sun Sep 12 13:54:12 2021

@author: rhyno
"""
#%% Functions

def get_user_info():
    user_name = input("Enter user name: \n")
    user_age = input("Enter user age: \n")
    print("\nYou are " + user_name + ", who is " + user_age + " years old!")


def addition():
    num_1 = float(input("Enter a number: \n"))
    num_2 = float(input("Enter another number: \n"))
    total = int(num_1 + num_2)
    print("The sum of the numbers is : " + str(total))


def compute_average():
    num_1 = float(input("Enter a number: \n"))
    num_2 = float(input("Enter another number: \n"))
    num_3 = float(input("Enter another number: \n"))
    num_4 = float(input("Enter another number: \n"))
    num_list = [num_1, num_2, num_3, num_4]
    avg = sum(num_list) / len(num_list)
    print("The average of the numbers is " + str(avg))


def compute_average_list(lst):
    avg = sum(lst) / len(lst)
    print("The average of the numbers is " + str(avg))


def degC_to_degF(c):
    f = c * 1.8 + 32
    print(str(c) + 'deg C is equal to ' + str(f) + 'deg F')

#%% Other

numbers = [1, 2, 44.5, 12]
average = sum(numbers) / len(numbers)
print('The average of the numbers is ' + str(average))





