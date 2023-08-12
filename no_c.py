def no_c(my_strings):
    new_string = ""
    for char in my_strings:
        if char != 'c' and char != 'C':
            new_string += char
    return new_string


print(no_c("Best School"))
print(no_c("Chicago"))
print(no_c("C is fun!"))
