#!/usr/bin/python3
#this code illustrates the 
#function that deletes the 
#item at a specific position in a list.
def delete_at(my_list=[], idx=0):
    if idx < 0:
        return my_list[:]
    elif idx >= len(my_list):
        return my_list[:]
    else:
        new_list = my_list[:]
        #del new_list[idx]
        #return new_list
        del my_list[idx]
        return my_list
        

my_list = [1, 2, 3, 4, 5]
idx = 3
new_list = delete_at(my_list, idx)
print(new_list)
print(my_list)