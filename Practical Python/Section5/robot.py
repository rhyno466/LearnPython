# -*- coding: utf-8 -*-
"""
Created on Sat Sep 25 17:11:25 2021

@author: rhyno
"""


class Robot:
    def __init__(self, name, version_number):
        self.name = name
        self.version_number = version_number
        self.internal_temperature = 23.0

    def say_hi(self):
        print("Hello, my name is " + self.name + ", ready to help!")

    def init_hardware(self):
        print("Init hardware!")

    def print_info(self):
        self.say_hi()
        print("Version Number: " + str(self.version_number))
        print("Internal Temp: " + str(self.internal_temperature))


class RoboticArm(Robot):
    def __init__(self, name, version_number, reach):
        super().__init__(name, version_number)
        self.reach = reach

    def pick_object(self, x, y):
        print("Pick object on (" + str(x) + ", " + str(y) + ")")

    def place_object(self, x, y):
        print("Place object on (" + str(x) + ", " + str(y) + ")")


class PackageSolution:
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def package(self, pick_x, pick_y, middle_x, middle_y, place_x, place_y):
        self.right.pick_object(pick_x, pick_y)
        self.right.place_object(middle_x, middle_y)
        self.left.pick_object(middle_x, middle_y)
        self.left.place_object(place_x, place_y)
