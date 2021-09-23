# -*- coding: utf-8 -*-
"""
Created on Sun Sep 12 13:54:12 2021

@author: rhyno
"""


def get_user_info():
    user_name = input("Enter user name: \n")
    user_age = input("Enter user age: \n")
    print("\nYou are " + user_name + ", who is " + user_age + " years old!")


def addition():
    num_1 = float(input("Enter a number: \n"))
    num_2 = float(input("Enter another number: \n"))
    total = int(num_1 + num_2)
    print("The sum of the numbers is : " + str(total))
