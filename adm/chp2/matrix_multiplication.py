# matrix multiplication
# let us assume we have matrix A of i,k and B of k,j dimensions
def matrix_mult(A, B):
    x = len(A)
    y = len(A[0])
    
    #get dimensions of matrix B
    y_prime = len(B) # rows in B
    z = len(B[0]) #columns of B
    
    #initialize C matrix
    C = [[0 for _ in range(z)] for _ in range(x)]
    
    # read the comments from bottom up
    # for all rows of A
    for i in range(0, x):
        # for all columns of B
        for j in range(0, z):
            # for all columns of A in selected row (outer loop)
            for k in range(0, y):
                # multiply element with common col in A and row in B
                C[i][j] += A[i][k] * B[k][j]
    return C
    
A = [[1,2],[3, 4]]
B = [[5,6,7],[8,9,10]]
C = matrix_mult(A,B)
for row in range(0, len(C)):
    print(str(C[row]) + ' row' + str(row) + '\n')
