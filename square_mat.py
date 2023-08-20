def square_matrix_simple(matrix=[]):
    new_met = []
    for row in matrix:
        new_row = [x**2 for x in row]
        new_met.append(new_row)

    return (new_met)

#!/usr/bin/python3
square_matrix_simple =square_matrix_simple

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

new_matrix = square_matrix_simple(matrix)
print(new_matrix)
print(matrix)