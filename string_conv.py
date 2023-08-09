#enter a string to hide in uppercase: HIDE
from urllib.parse import scheme_chars


string = input("Enter a string to hide in Uppercase: ")
s_code = ""
#cycle through each character
for char in string:
    s_code += str(ord(char))
                 
#Secrete Message : 35647890
print("secrete message : {}".format(s_code))

#cycle through each character code 2 at a time by incrementing 2 at a time
norm_string = ''
for i in range(0, len(s_code)-1, 2):
    char_code = s_code[i] + s_code[i+1]
    #convert the code into characters and add them to a new string
    norm_string += chr(int(char_code))
#original message: HIDE
print("Normal message: {}".format(norm_string))