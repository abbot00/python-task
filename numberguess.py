#!/usr/bin/python3
#this is an example of an implementation of a do while loop
#this code prompts the user for an integer between 1 and 10 and compares the user's integer to a set of random numbers 
import random
while True:
    num1 = int(input("input a number between 1 to 10: "))
    num2 = random.randint(1,10)
    if (num1 == num2):
        print("you guesed righ!! {} : {}".format(num1, num2))
        break
    print("please try again!")
    