# Ask the user to input 2 values and store them in variables num1 and num2
num1, num2 = input('Enter two numbers:').split()

#convert the strings into regular numbers integer
num1 = int(num1)
num2 = int(num2)
# add the values entered and store in sum
sum = num1 + num2

# Subtract values and store in difference
difference = num1 - num2

#multiply the values and store in product

product = num1 * num2
#divide the values and store in quotient

quotient = num1 / num2
#use modulus on the values and store in remainder
remainder = num1 % num2
#print the answers
print("{} + {} = {}".format(num1, num2, sum))
print("{} - {} = {}".format(num1, num2, difference))
print("{} * {} = {}".format(num1, num2, product))
print("{} / {} = {}".format(num1, num2, quotient))
print("{} % {} = {}".format(num1, num2, remainder))

