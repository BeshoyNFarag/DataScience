'''
Challenge 1 — Row and Column Operations
Create a 5*5 array of random integers between 1 and 50.
Compute the sum of each row and each column separately.
Replace the last column with the column sums.
Replace the last row with the row sums.

import numpy as np
array = np.random.randint(1, 50, (5, 5))
print(array)
row = []
column = []
for each_arr in array:
    row.append(np.sum(each_arr))
for x in range(5):
    column.append(np.sum(array[:, x]))
print(row)
print(column)
array[:, -1] = column
array[-1, :] = row
print(array)


Challenge 2 — Masking and Filtering
Create an array of 30 random integers between 0 and 100.
Extract only the numbers that are divisible by both 2 and 3.
Count how many numbers satisfy that condition.
Replace all numbers greater than 80 with 0.

import numpy as np

array_rand = np.random.randint(0, 101, 30)
array = []
count = 0

for x in array_rand:
    if x % 2 == 0 and x % 3 == 0:
        array.append(x)
        count += 1

print(array_rand)
print(array)
print("\n")

for x in range(30):
    if array_rand[x] > 80:
        array_rand[x] = 0


print(array_rand)





Challenge 3 — Normalization
Create an array of random floating-point numbers (shape 4×4).
Normalize it so that all values are between 0 and 1
(subtract the minimum and divide by the range).
Verify that the minimum value is 0 and the maximum value is 1.

# to normalize we need to subtract the matrix by its minimun then divide it by the maximum minus the minimum

import numpy as np

array_rand = np.random.random((4, 4))
max_val = np.max(array_rand)
min_val = np.min(array_rand)
print(array_rand)
normalized_arr = (array_rand - min_val)/(max_val - min_val)
print(normalized_arr)



Challenge 4 — Fancy Indexing
Create an array with values from 10 to 100 (inclusive).
Select all elements whose index is a multiple of 3.
Multiply those selected elements by −1.
Replace them back into the original array.

import numpy as np

array = np.arange(10, 101)

for x in range(array.size - 1):
    if x % 3 == 0 and not x == 0:
        array[x] *= -1

print(array)



Challenge 5 — Matrix Logic
Create a 3×3 matrix of random integers between −5 and 5.
Replace all negative numbers with their absolute values.
Then, replace all even numbers with 0.
Count how many zeros are in the matrix.

import numpy as np


array = np.random.randint(-5, 6, (3, 3))

print(array)


for x in range(3):
    for y in range(3):
        if array[x, y] < 0:
            array[x, y] = abs(array[x, y])


print(array)



Challenge 6 — Combining Arrays
Create one 2×3 array full of ones and another 2×3 array full of twos.
Combine them vertically, then horizontally.
After that, reshape the result into a single 3×4 array.
####there are functions called vstack and hstack that is about it for this challenge




Challenge 7 — Statistical Operations
Create an array of 100 random numbers.
Find the mean, median, variance, and standard deviation.
Subtract the mean from every element (center the data).
Verify that the new array’s mean is approximately 0.

import numpy as np
import random as rand


size = rand.randint(5, 20)
array = np.random.randint(0, 100, size)

mean = np.mean(array)
median = np.median(array)
variance = np.var(array)
standard_dev = np.std(array)
print(array)
print(mean)

array = array - mean

mean = np.mean(array)
print(array)
print(mean)



Challenge 8 — Conditional Replacement
Make a 6×6 array of random integers between 0 and 20.
Replace:
All numbers less than 5 with −1
All numbers between 5 and 10 with 0
All numbers greater than 10 with 1
Count how many of each category exist.

import numpy as np

array_rand = np.random.randint(0, 21, (6, 6))

print(array_rand)


for i in range(6):
    for j in range(6):
        if array_rand[i, j] < 5:
            array_rand[i, j] = -1
        elif array_rand[i, j] > 5 and array_rand[i, j] < 10:
            array_rand[i, j] = 0
        elif array_rand[i, j] > 10:
            array_rand[i, j] = 1

print(array_rand)


Challenge 9 — Advanced Reshaping
Create an array with numbers from 0 to 63.
Reshape it into a 4D array of shape (2, 2, 4, 4).
Extract the second “block” (the one with index 1 in the first dimension).
Within that block, reverse the order of the last two axes.

'''

import numpy as np

array = np.arange(64)
print(array)
array = array.reshape(2, 2, 4, 4)
print(array)
