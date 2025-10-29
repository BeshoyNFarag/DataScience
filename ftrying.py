'''
ndim ===> it gives you the number of dimesions a certain array has
.shape gives you the dimensions
.dtype gives you the data type of the array
b = np.array([1, 2, 3], dtype="int16") ====> this specifies the data type that we will be using
.size the number of elements
a [0, : ]  ==> the first row and the entire columns
np.zeros(the shape)
np.ones(also the shape)
np.full(the shape, the number to fill the array)
np.random.rand(the shape)

np.random.randint(between, to, size = (shape))
np.repeat()

dont say array1 = array2 cause this will make your 2 arrays as one instead do array1 = array2.copy()
np.arange(10) this makes a list that is from 0 before 10
np.arange(15).reshape(3,5) this makes the list from 0 to 15 but split into 3 rows and 5 columns
np.exp(a) ==> makes all the numbers inside the array a powered by e

'''


import numpy as np

rng = np.random.default_rng(150)
d = rng.uniform(low=0.0, high=2.0, size=4)
print(d)
