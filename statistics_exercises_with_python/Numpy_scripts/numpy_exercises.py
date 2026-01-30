import numpy as np
# Create a 1D array of integers from 0 to 4
a = np.array([1, 2, 3, 4])

a.dtype
a.ndim

a.shape
f = np.array([12.2,4.3,7.5,9.6])
a + f
a * f

# operation can be done between array and scalar, for instance
a * 10

# Universal Functions (ufuncs)
np.sin(a)

# Multi-Dimensional Arrays
a = np.array([[0,1,2,3],[10,11,12,13]])

a.shape

a[1,3]
a[1]
a[1,3]

# Slicing
a = np.array([11,12,13,14,15])
a[1:3]

# negative indices work also
a[1:-2]
a[-4:3]

# grab first three elements
a[:3]

# grab the last 2 elements
a[-2:]

# 2 d array

a = np.arange(25).reshape(5,5)
a[:,1::2]
a[4,:]
a[1::2,:3:2]

a = np.array([0,1,2,3,4])

# use slicing for insert iterable of lenght of two
a[-2:] = [-1,-2]
a

# ora a scalar value
a[-2:] = 99
a
