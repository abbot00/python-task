#!/usr/bin/python3
"""" ceser cyfer project
encrypts a series of strings for the user and dycripts at the reciveing end
#we do this by shifting each alphabet of the string a number of spaces on the unicode 
#A -Z 65 -90
#a - z 97 - 122
# ord(your_letter): converts each letter to its unicode version
# chr(your_code): converts each code back to its letter representation

#hints
#use isupper() to decide which unicodes to work with
#add the key(number of characters to shift) and if the key is bigger or smaller then the unicode for 
#A, Z, a, z increase or decrease by 26
"""
#recieve the message to encrypt and the number of caracters to shift
#ask user t0 input words
def encrypt(message = input("enter your message: ") , key  = int(input("enter your encryption key (between 1- 26): "))):
  
    #prepare the secret_message
    sec_message = ""
    #cycle through each character in the message
    for char in message:
    

        #if it isnt a letter then keep it as it is
        if char.isalpha():

             #get the character code and add the shift amout
            char_code = ord(char)
            char_code += key 
            #if uppercase then compare to uppercase unicodes 
            if char.isupper():
                
                #if bigger than Z subtract 26
                if char_code > ord('Z'):
                    char_code -= 26
                #if smaller than A add 26
                if char_code < ord('A'):
                    char_code += 26


            #do the same for lowercase characters
            else:
                 #if bigger than z subtract 26
                if char_code > ord('z'):
                    char_code -= 26
                #if smaller than a add 26
                if char_code < ord('a'):
                    char_code += 26



        #convert from code to letter and add to message
            sec_message += chr(char_code)

        #if not a letter leave character as is
        else:
            sec_message += char
    print("Encrypted : {}".format(sec_message))


def decrypt(sec_message , key):
    # to decrypt the only thing that changes isthe sign of the key
    key = -key
    message = ""
    for char in sec_message:
    

        #if it isnt a letter then keep it as it is
        if char.isalpha():

             #get the character code and add the shift amout
            char_code = ord(char)
            char_code += key 
            #if uppercase then compare to uppercase unicodes 
            if char.isupper():
                
                #if bigger than Z subtract 26
                if char_code > ord('Z'):
                    char_code -= 26
                #if smaller than A add 26
                if char_code < ord('A'):
                    char_code += 26


            #do the same for lowercase characters
            else:
                 #if bigger than z subtract 26
                if char_code > ord('z'):
                    char_code -= 26
                #if smaller than a add 26
                if char_code < ord('a'):
                    char_code += 26



        #convert from code to letter and add to message
            message += chr(char_code)

        #if not a letter leave character as is
        else:
            message += char
    print("Decrypted : {}".format(message))

encrypt("jude is here", 5)