import random

def generate_random_matrix(rows, cols):
    return [[random.randint(1, 10) for _ in range(cols)] for _ in range(rows)]

def matrix_multiply(matrix1, matrix2):
    rows_matrix1 = len(matrix1)
    cols_matrix1 = len(matrix1[0])
    cols_matrix2 = len(matrix2[0])

    result = [[0] * cols_matrix2 for _ in range(rows_matrix1)]

    for i in range(rows_matrix1):
        for j in range(cols_matrix2):
            for k in range(cols_matrix1):
                result[i][j] += matrix1[i][k] * matrix2[k][j]

    return result

# Input matrix dimensions
rows1 = int(input("Enter the number of rows for Matrix 1: "))
cols1 = int(input("Enter the number of columns for Matrix 1: "))
rows2 = int(input("Enter the number of rows for Matrix 2: "))
cols2 = int(input("Enter the number of columns for Matrix 2: "))

# Check if multiplication is possible
if cols1 != rows2:
    print("Matrix multiplication is not possible with these dimensions.")
else:
    matrix1 = generate_random_matrix(rows1, cols1)
    matrix2 = generate_random_matrix(rows2, cols2)

    print("Matrix 1:")
    for row in matrix1:
        print(row)

    print("\nMatrix 2:")
    for row in matrix2:
        print(row)

    result = matrix_multiply(matrix1, matrix2)
    print("\nResult of multiplication:")
    for row in result:
        print(row)
