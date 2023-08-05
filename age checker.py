#if age is 5 Go to Kindergarten
#Ages 6 through 17 goes to grades 1 through 12
#if age is greater than 17 say go to colage
#try to complete with 10 or less lines
 
#prompt the user to input age
age = eval(input("How old are you? "))

#check if age is less than 5
if age < 5:
    print("Too young for school")

#check if age is  equals to 5
elif age == 5:
    print("go to Kindergarten")


#check if age is betweeen 6 and 18
grade = age - 5
if (age >= 6) and (age <= 17):
    print("go to {} grade".format(grade))
else:
    print ("go to collage")
