"""this code creates a list of 5 random numbers any time its ran"""
import random
import math

list1 = list(range(5))#creates an empty list that has the range of 5 inputs
for i in range (5):
    list1[i] = random.randint(1, 10)
for i in list1:
    print(i)
print("list1 = {}".format(list1))


