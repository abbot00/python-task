#store the user input of 2 numbers and the operator
num1, opperator, num2 = input("Enter calculation").split()

#Convert the strings to integers
num1 = int(num1)
num2 = int (num2)

#if + then we need to provide ouptut based on addition
if opperator == "+":
    print ("{} + {} = {}".format(num1,num2,num1+num2))
elif opperator == "-":
     print ("{} - {} = {}".format(num1,num2,num1-num2))
elif opperator == "*":
     print ("{} * {} = {}".format(num1,num2,num1*num2))
elif opperator == "/":
     print ("{} / {} = {}".format(num1,num2,num1/num2))
else:
     print("use either + - / or * next time")

#print result