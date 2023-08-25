import numpy as np
#This is a matrix but as in a dictionary 
#The outer set of integers are the rows
#The first set of intergers within the second set of brackets represents the column header

matrix_A = {
    0: {0: 1, 1: 2, 2: 3},
    1: {0: 4, 1: 5, 2: 6},
    2: {0: 7, 1: 8, 2: 9}
}
array_A = np.array(matrix_A)

print(array_A)
print(array_A.shape)
print(array_A.ndim)

#This the equivalent with arrays in numpy the blue brackets are the rows


import numpy as np

matrix = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])

print(matrix)
print(matrix.shape)
print(matrix.ndim)




