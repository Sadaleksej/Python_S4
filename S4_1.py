def transpose_matrix(matrix):
    if not matrix:
        return []
    
    rows = len(matrix)
    cols = len(matrix[0])
    
    transposed = [[matrix[j][i] for j in range(rows)] for i in range(cols)]
    
    return transposed


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
transposed_matrix = transpose_matrix(matrix)

for row in transposed_matrix:
    print(row)
