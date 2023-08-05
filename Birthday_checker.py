# we will provide different output based on age
# 1 - 18 -> Important
#21, 50, > 65 -> Important
#All others -> Not important


#Recieve age and store in age
age = eval(input("enter age:"))
#and: if both conditions are true it returns true
#or: if either condition is true then it returns true
#not: convert a true conditon into false or vise verse


# if age is both greater than or equal to 1 and less than or equal to 18 Important
if (age >= 1) and (age <= 18):
    print("Important Birthday")
#if age is either 21 or 50 Important
elif (age == 21) or (age == 50):
    print("Important Birthday")
#We check if age is less than 65 and then convert true to false and vice versa
elif not(age < 65):
    print("important birthday")


#else, Not important
else:
    print ("Sorry Not Important Birthday")
    