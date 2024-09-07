def reflectOverSecondaryDiagonal(matrix):
    size = len(matrix)
    new_matrix = []
    for i in range(size-1, -1, -1):
        row = []
        for j in range(len(matrix[0])-1, -1, -1):
            print(f"i: {i}, j: {j} : {matrix[i][j]} --{matrix[j][i]} ")
            row.append(matrix[j][i])
        new_matrix.append(row)
    return new_matrix

# Example square matrix to reflect over the secondary diagonal
square_matrix = [
 [1, 2, 3],
 [4, 5, 6],
 [7, 8, 9]
]

# Call the function and print the transformed matrix
# TODO: Call the function on square_matrix and store the result in transformed_matrix.
transformed_matrix = reflectOverSecondaryDiagonal(square_matrix)
print(transformed_matrix)
# Output should be:
# [
#  [9, 6, 3],
#  [8, 5, 2],
#  [7, 4, 1]
# ]