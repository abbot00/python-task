def add_tuple(tuple_a=(), tuple_b=()):
    #make sure tuples have at least 2 elements
    a = tuple_a[:2] + (0, 0)[:2 - len(tuple_a)]
    b = tuple_b[:2] + (0, 0)[:2 - len(tuple_b)]

    result = (a[0] + b[0], a[1] + b[1])
    return result

tuple_a = (1, 89)
tuple_b = (88, 11)
new_tuple = add_tuple(tuple_a, tuple_b)
print(new_tuple)

print(add_tuple(tuple_a, (1, )))
print(add_tuple(tuple_a, ()))
