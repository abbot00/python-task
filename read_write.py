import os
with open("mydata.txt",mode='w', encoding="utf-8") as myfile:
     myfile.write("this is an exampl of write and read in python {}".format(os.getcwd()))

with open("mydata.txt",encoding="utf-8") as myfile:
    print(myfile.read())

print(os.getcwd())