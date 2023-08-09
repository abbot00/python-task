#!/usr/bin/python3
#draw a pine tree on screen 

#gets the lengt of the tree from user
hight = input("how tall in the tree: ")

#convert into integer
hight = int(hight)
#get starting spaces
spaces = hight - 1
#one harsh to start that will be incremented
hash = 1 
#save stump spaces till later
stump_spaces = hight - 1
#make sure the right number of rows is printed
while hight != 0:
    
#print the spaces
    for i in range(spaces):
        print(' ', end='') 
#print the hashes
    for i in range(hash):
        print("#",end = ' ')
#new line afte each row is printed
    print()
#spaces decremeted by 1 each time
    spaces -= 1
#the hashes is incremented by 2 each time
    hash += 2
#decrement tree hight each time to jump out of the loop
    hight -= 1
#print the spaces before the stump and then the harsh
for i in range(stump_spaces):
    print(" ", end='')
print('#')
