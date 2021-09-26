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


#%% For Loop
my_list = [1, 2, 3, "ahhm", 4.5]

for elem in my_list:
    print(elem)

print("Done")

for elem in range(10):
    print(elem)

for elem in range(1, 10, 2):
    print(elem)


#%% While Loops
my_list = [10, 2, 30, 5, 12]

cum_mul = 1
current_elem = 0
while cum_mul < 100:
    cum_mul *= my_list[current_elem]
    print(cum_mul)
    current_elem += 1

#%%
for i in range(10):
    print(i)

i = 0
while i < 10:
    print(i)
    i += 1

my_list = [10, 20, 30, 5, 5, 20, 40]

index = 0
res_add = 0
while res_add < 70:
    res_add = res_add + my_list[index]
    index += 1
    print(res_add)
print(index)

#%%
my_list = [1, 2, 3, "stop", 3.42, 4, 5, "stop"]

for cur_elem in my_list:
    print(cur_elem)
    if cur_elem == "stop":
        print("the loop will NOT continue")
        break
print("outside of the loop")

index = 0
while index < len(my_list):
    cur_elem = my_list[index]
    print(cur_elem)
    if cur_elem == "stop":
        print("the loop will stop")
        break
    index += 1

#%%
my_list = [1, 2, 3, "stop", 3.42, 4, 5, "stop"]

for cur_elem in my_list:
    if cur_elem == "stop":
        print("the loop will NOT stop")
        continue
    if type(cur_elem) != int:
        print("the loop will NOT stop for non ints")
        continue
    print(cur_elem)
print("outside of the loop")

#%% ZIP FUNCTION

first = [1, 2, "stop", 3.42, 5, 12]
sec = [5, 1, 10, 3]
zipped_lists = zip(first, sec)
# print(list(zipped_lists))

for e1, e2 in zipped_lists:
    print(e1, e2)

#%% zip

l1 = [1, 3, 2]
l2 = [5, 1, 4]
zl = zip(l1, l2)
# print(list(zl))

for i1, i2 in zl:
    print(i1, i2)

#%% emumerate
my_list = [1, 2, 3, "stop", 3.42, 4, 5, "stop"]
print(list(enumerate(my_list)))

for cnt, elem in enumerate(my_list):
    print(elem, cnt)


#%% list comprehension

ml_norm = []

for elem in range(20):
    ml_norm.append(elem)

ml_comp = [elem + 1 for elem in range(20)]

print(ml_norm)
print(ml_comp)

#%%


