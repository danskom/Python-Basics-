#Tensors 

#tensor as a dictionary     

import numpy as np

tensor = {
    0: {0: [[1, 2, 3], [4, 5, 6]],
        1: [[7, 8, 9], [10, 11, 12]]},
    1: {0: [[13, 14, 15], [16, 17, 18]],
        1: [[19, 20, 21], [22, 23, 24]]}
}

array_A = np.array(tensor)

print(array_A.shape)  
print(array_A.dtype)
print(array_A)

import numpy as np

tensor_array = np.array([
    [[1, 2, 3], [4, 5, 6]],
    [[7, 8, 9], [10, 11, 12]],
    [[13, 14, 15], [16, 17, 18]],
    [[19, 20, 21], [22, 23, 24]]
])

tensor_array = tensor_array.reshape((2, 2, 2, 3))  # Reshape to match the original tensor dimensions

print(tensor_array)
print(tensor_array.shape)
print(tensor_array.ndim)

array_2 = ([[[ 1,  2,  3],
        [ 4,  5,  6]],

       [[ 7,  8,  9],
        [10, 11, 12]],

       [[13, 14, 15],
        [16, 17, 18]],

       [[19, 20, 21],
        [22, 23, 24]]])

tensor_array_2 = tensor_array.reshape((2, 2, 2, 3)) 

print(tensor_array_2)
print(tensor_array_2.shape)
print(tensor_array.ndim)
