#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 28 21:06:43 2021

@author: rhyno466
"""
#%% line strut
x = 1
y = 1

z = 1

# this is a comment

b = 1 + 2
c = 1 + 2

r = 1
v = 3
oo = 9.0
#%% comments
summing = 3 + 4  # this lines sums 2 nums

# this is a comment line

"""
lots if comments

a shit tonne
"""

#%% joining lines
x = 4
y = 3

z = x + y

#%% mult statement single line
x = 3
y = 4
z = x + y


#%% indentation

#%% variables
x = 4 + 5
print(x)
result_two = 4 + 4

#%% int and float
x = 1.0
y = 1
z = x * y
print(type(x))
print(z)
print(type(z))

#%% strings

g = "i'm a \nprogrammer"
print(g)

f_str = "a"
s_str = "b"

print(type(f_str))
print(f_str + "\n" + s_str)

#%% str manipulation
a = "first"
b = "second"
c = a + b
d = a * 3
print("f" in d)
print(len(d))
print(str(1.0))

#%% str index

a = "ryne is really cool"
print(a[1])
print(a[-2])

#%% str slicing

a = "ryne is really cool and is living the fucking dream"
print(len(a))
print(a[0:8])
print(a[0:10:2])
print(a.count("r"))
print(a.find("r"))
print(a[-5:-1])

#%% booleans

a = "ryne is really cool and is living the fucking dream"
b = "f" in a
g = True
print(b)
print(type(b))
print(type(g), g)
x = 3
y = 4
z = x == y
print(z, type(z))

#%%

x = 5.0
print(x)
print(f"The current value of X is {x}")
nme = "ryne"
a = "{nme} is really cool and is living the fucking dream"
b = a.format(nme="kari")
print(a)
print(b)
