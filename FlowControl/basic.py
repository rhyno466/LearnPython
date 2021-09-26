# -*- coding: utf-8 -*-
"""
Created on Sun Sep 26 09:09:46 2021

@author: rhyno
"""

x = 10
y = 20
z = 30

if y > x:
    print(y)
elif z > y:
    print(z)
else:
    print(x)

if y > x:
    print("First Block")

    if z > y:
        print(z)
    elif x > y:
        print(x)
    print("Also first block")
print("block zero")

#%%
my_list = ["1", 1, 1.0]

if 1 in my_list:
    print(my_list)

z = 10
x = 1
y = 5

if x > y and z > y:
    print("this")
elif x > y or z > y:
    print("that")


#%%
my_list = [1, 2, 3, "ahhm", 4.5]

for elem in my_list:
    print(elem)

print("Done")

for elem in range(10):
    print(elem)

for elem in range(1, 10, 2):
    print(elem)
