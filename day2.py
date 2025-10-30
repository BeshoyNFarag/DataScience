'''Exercise 1 — Array Info
Create a 2D array with two rows and three columns.
Print its number of dimensions.
Print its shape.
Print its data type.
Print how many elements it contains.


#code starts here

import numpy as np

array1 = np.array([[1, 2, 3], [4, 5, 6]])

print(f"the number of dimensions is: {array1.ndim}")
print(
    f"the shape which means how many rows to columns it contains is: {array1.shape}")
print(f"the data type of the array is: {array1.dtype}")
print(f"the number of elements is: {array1.size}")


Exercise 2 — Zeros, Ones, Full
Create a 3×3 array full of zeros.
Create a 2×4 array full of ones.
Create a 4×4 array filled with the number 7.


import numpy as np

array_zeros = np.zeros((3, 3))
array_ones = np.ones((2, 4))
array_seven = np.full((4, 4), 7)

print(array_zeros)
print(array_ones)
print(array_seven)



Exercise 3 — Random Arrays
Create a random array with shape 3×3 using random floating-point numbers.
Create another random array with shape 2×5 containing random integers between 10 and 50.
Print the shape and data type of both arrays.


import numpy as np

rand_array = np.random.randint(0, 11, (3, 3))
rand_array2 = np.random.randint(10, 51, (2, 5))
print(rand_array2)

Exercise 4 — Indexing and Slicing
Make an array that goes from 0 to 14 and reshape it into 3 rows and 5 columns.
Print the first row.
Print the last column.
Print the middle row.
Print the element in the second row, third column.


import numpy as np

array = np.array([x for x in range(15)]).reshape((3, 5))
print(f"print the entire array: {array}")
print(f"print the first row: {array[0,:]}")
print(f"print the last column: {array[:,-1]}")
print(f"print the middle row: {array[1, :]}")
print(f"print the element in the second row and third column: {array[1,2]}")


Exercise 5 — Repeat and Copy
Create a 1D array with three elements.
Repeat each element three times.
Make a true copy of that array, modify one of them, and print both to show they are independent.

import numpy as np

array = np.array([1, 3, 5])
array2 = array.copy()
array = array.repeat(3)
print(array)
print(array2)



Exercise 6 — Exponential
Create an array with values from 0 to 3.
Apply the exponential function to it and observe the results.

import numpy as np

array = np.array([x for x in range(4)])
array = np.exp(array)
print(array)



Exercise 7 — Mini Challenge
Create an array containing the numbers from 0 to 20.
Reshape it into 4 rows and 5 columns.
Replace all even numbers with 0.
Apply the exponential function to the final array.
'''

import numpy as np

array = np.arange(20)
array = array.reshape(4, 5)
sorted_np = []

for x in array:
    for y in x:
        if y % 2 == 0:
            sorted_np.append(0)
        else:
            sorted_np.append(y)


array2 = np.array(sorted_np)
print(array2)
