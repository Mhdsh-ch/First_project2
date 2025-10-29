def matrix_multiply(A, B):
    result = [[0 for _ in range(len(B[0]))] for _ in range(len(A))]
    for i in range(len(A)):           
        for j in range(len(B[0])):   
            for k in range(len(B)):   
                result[i][j] += A[i][k] * B[k][j]   
    return result
def print_matrix(matrix):
    for row in matrix:
        print(row)
A = [
    [1, 2, 3],
    [4, 5, 6]
]
B = [
    [7, 8],
    [9, 10],
    [11, 12]
]

print("matris A:")
print_matrix(A)

print("\matris B:")
print_matrix(B)

print("\nresult (A × B):")
result = matrix_multiply(A, B)
if result:
    print_matrix(result)