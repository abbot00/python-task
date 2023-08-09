# problem: recieve number in miles and convert to kilometer
#kilometers = miles * 1.60934
#prompts the user to enter miles
miles = input("Eniter Miles ")

#converst miles string to int
miles = int(miles)

#converst the miles to kilometers
kilometers = miles * 1.60934
#print the output
print("{} miles equals {} kilometers".format(miles, kilometers))