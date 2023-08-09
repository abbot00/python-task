#!/usr/bin/python3
while True:
    try:
        
        number = int(input("enter a number: "))
        break
    except ValueError:
        print("upi didnt enter a number")
    except:
        print("An unknown error occored")
print("thank you for entering a number")