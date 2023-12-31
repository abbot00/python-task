def element_at(my_list, idx):
    if idx < 0:
        return None
    elif idx > (len(my_list) - 1):
        return None
    else:
        return my_list[idx]

def replace_in_list(my_list, idx, element):
    if idx < 0:
        return my_list
    elif idx > (len(my_list)):
        return my_list
    else:
        my_list[idx] = element
        return my_list
"""my_list = [1, 2, 3, 4, 5]
idx = 3
print("Element at index {:d} is {}".format(idx, element_at(my_list, idx)))
"""

my_list = [1, 2, 3, 4, 5]
idx = 3
new_element = 9
new_list = replace_in_list(my_list, idx, new_element)

print(new_list)
print(my_list)