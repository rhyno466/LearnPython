# -*- coding: utf-8 -*-
"""
Created on Sat Sep 25 16:50:46 2021

@author: rhyno
"""


from robot import Robot
from robot import RoboticArm
from robot import PackageSolution

#%%

jeff = Robot("Jeff", 2.0)
# jeff.say_hi()
# jeff.init_hardware()
# jeff.print_info()

ryan = Robot("Ryan", 1.0)
# ryan.print_info()

rynes_arm = RoboticArm("Ryne", 2.0, 32.6)
allisons_arm = RoboticArm('Allsion', 2.0, 33)

pack = PackageSolution(rynes_arm, allisons_arm)
pack.package(2, 4, 6, 8, 12, 20)


