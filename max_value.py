#this is an illustration of a function that returns the max value in a list of integers
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    else:
        max_value = my_list[0]
        for num in my_list[1:]:
            if num > max_value:
                max_value = num
        return max_value 

    
my_list = [1, 90, 2, 13, 34, 5, -13, 3]
max_value = max_integer(my_list)
print("Max: {}".format(max_value))
