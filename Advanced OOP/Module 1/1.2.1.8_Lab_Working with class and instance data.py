'''
Estimated time

20 minutes
Level of difficulty

Easy
Objectives

    creating classes, class and instance variables;
    accessing class and instance variables;

Scenario

Imagine that you receive a task description of an application that monitors the process of apple packaging before the apples are sent to a shop.

A shop owner has asked for 1000 apples, but the total weight limitation cannot exceed 300 units.

Write a code that creates objects representing apples as long as both limitations are met. When any limitation is exceeded, than the packaging process is stopped, and your application should print the number of apple class objects created, and the total weight.

Your application should keep track of two parameters:

    the number of apples processed, stored as a class variable;
    the total weight of the apples processed; stored as a class variable. Assume that each apple's weight is random, and can vary between 0.2 and 0.5 of an imaginary weight unit;

Hint: Use a random.uniform(lower, upper) function to create a random number between the lower and upper float values.

'''

import random

class Apple:
    number = 0
    
    def __init__(self):
        self.weight = random.uniform(0.2, 0.5)
        Apple.number += 1

number_limit = 1000  # 852 is the number of apples at which you can easily get both results quite often.
weight_limit = 300
precision = 2  # decimal precision

apples_weight = 0
for i in range(number_limit):
    apple = Apple()
    if round(apples_weight + apple.weight, precision) > weight_limit:
        print(f"Weight limit reached. Packed {Apple.number-1} apples of total weight {round(apples_weight, precision)}.")
        exit()
    apples_weight += apple.weight
    
print(f"Packed {Apple.number} apples of total weight {round(apples_weight, precision)}.")