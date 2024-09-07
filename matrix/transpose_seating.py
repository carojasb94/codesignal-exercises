# TODO: Define a function 'transpose_seating' that takes a 2D list 'arrangement' as its parameter.
    # TODO: Create a new 2D list 'transposed' with dimensions swapped (columns become rows and vice versa) filled initially with zeros.
def transpose_seating(matrix: list):
    print(matrix)
    result = [[0 for j in range(len(matrix))] for _ in range(len(matrix[0]))]
    print(result)
    for i in range(len(matrix[0])):
        for j in range(len(matrix)):
            result[i][j] = matrix[j][i]
    return result
    # TODO: Use nested loops to transpose each element from the original seating arrangement to the new arrangement 'transposed'.

# Restaurant seating before transposition (rows)
seating_before = [
 [1, 2],
 [3, 4],
 [5, 6]
]

# TODO: Print the 'transposed' arrangement to see the new seating arrangement.
print(transpose_seating(seating_before))
