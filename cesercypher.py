"""" ceser cyfer project
encrypts a series of strings for the user and dycripts at the reciveing end"""
#we do this by shifting each alphabet of the string a number of spaces on the unicode 
#A -Z 65 -90
#a - z 97 - 122
# ord(your_letter): converts each letter to its unicode version
# chr(your_code): converts each code back to its letter representation

#hints
#use isupper() to decide which unicodes to work with
#add the key(number of characters to shift) and if the key is bigger or smaller then the unicode for 
#A, Z, a, z increase or decrease by 26

