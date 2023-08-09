#enter a string to hide in uppercase: HIDE
string = input("Enter a string to hide in Uppercase: ")
s_code = ""
#cycle through each character
for char in string:
    s_code += str(ord(string))
                 
#Secrete Message : 35647890
print("secrete message : {}".format(s_code))

#original message: HIDE
