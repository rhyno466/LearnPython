#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  2 20:20:49 2021

@author: rhyno466
"""
# # Ask user name
# user_name = input("What is your name: ")

# # Ask user age
# user_age = input("WHhat is your age: ")

# # Print input
# print("\nHello " + user_name + " your are " + user_age + " years old!")


# # This is a comment

#%% Section 2.5


def say_hello(user_name, user_age):
    print("Hello " + user_name + " you're " + str(user_age))


def double_number(number):
    return number * 2


def print_double_number(number):
    result = double_number(number) #local car
    print("Double of " + str(number) + " is equal to " + str(result))


a = 2 #global var

# say_hello("Ryne", 33)
# say_hello("John", 23)

print_double_number(3)
print(result)
