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

import matplotlib.pyplot as plt

img = plt.imread("C:/Users/david/OneDrive/Documenti/Git/profile/statistics_exercises_with_python/Numpy_scripts/dc_metro.png")

def smooth(img):
    avg_img = (   img[1:-1 ,1:-1] #center
                + img[ :-2 ,1:-1] #top
                + img[2:   ,1:-1] #bottom
                + img[1:-1 , :-2] #left
                + img[1:-1 ,2:  ] #right
                 ) / 5.0
    return avg_img

smoothed = smooth(img)
plt.imshow(smoothed)
plt.show()

#fancy indexing
a = np.arange(0,80,10)
a

indices = [1,2,-3]
y = a[indices]
print(y)

#fancy indexing in 2d
a = np.arange(0,100).reshape(10,10) #2d array, rows by 10 elements each

a[[0,1,2,3,4],[1,2,3,4,5]]
a[3:, [0,2,5]]

# exercise
a = np.arange(25).reshape(5, 5)
a[[0,2,3,3],[2,3,1,4]]

# array calculation methon
a = np.array([[1,2,3],[4,5,6]])
a
a.sum()
a.sum(axis=0)
a.sum(axis=-1)

a = np.array([-1,2,5,5])
a == a.max()
np.where(a == a.max())
np.where(a > 0)

# reshape - return a new array
a = np.array([[0,1,2],[3,4,5]])
a.reshape(3,2)

# shape - similarly can be used to reshape the array:
a = np.arange(6)
a
a.shape = (2,3)
a

# flatten: take a multidimensional array and turn into a flat array
a.flatten()
a
