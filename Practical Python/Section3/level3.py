#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 22 20:46:40 2021

@author: rhyno46655
"""

user_age = 176
month = "May"

if user_age >= 18:
    print("You are an adult")
else:
    print("You are not an adult yet")

if month in ["June", "July", "August"]:
    print("Summer Time")
elif month in ["September", "October", "November"]:
    print("Autumn Time")
elif month in ["December", "January", "February"]:
    print("Winter Time")
else:
    print("Spring Time")


print("End of Porgram")
