# NUMPY- Numerical PYTHON
# PYTHON LIBRARY, WORKING WITH ARRAYS
# Domain - Algebra, Fourier Transform, Matrices
# NUMPY Provides array object,50x faster than lists in python
# ndarray

# pip install numpy

import numpy as np

arr = np.array([2, 34, 5, 8, 59])
print("Numpy Example")
print(arr)


# Checking Numpy Version
print("Numpy Version")
print(np.__version__)


# NUMPY Creating Arrays
arr = np.array([1, 2, 3, 4, 5])
print(arr)
print(type(arr))

# Creating a Rank 1 Array
arr = np.array([1, 2, 3])
print("Array with Rank1: \n", arr)

# Creating a Rank 2 Array
arr = np.array([[1, 2, 3],
                [4, 5, 6]])
print("Array with Rank 2: \n", arr)


# using tuple to create numpy
arr = np.array((10, 11, 12, 13, 14))
print("Array Created using passed tuple \n", arr)


#Dimensions in Arrays

# O-D Arrays or Scalar
# Elements in the array, each value in an array is 0-D Array

arr = np.array(42)
print(arr)

#Output - 42

# 1-D Arrays
# Basic Array or Uni-Dimensional Array

arr = np.array([20, 30, 40, 50])
print(arr)


# 2-D Arrays
# Matrix

arr = np.array([[11, 22, 33], [44, 55, 66]])
print(arr)


# 3-D Arrays
# A Array that has 2-D Array or Matrices as its elements
# 3rd order tensor

arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(arr)


# Check Number of Dimensions
# ndim attribute

a = np.array(42)
b = np.array([1, 2, 3])
c = np.array([[1, 2, 3], [4, 5, 6]])
d = np.array([[[1, 2, 3], [4, 5, 6], [70, 8, 9]]])

print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)

# 5-D Dimension Array

arr = np.array([2, 4, 6, 8], ndmin=5)
print(arr)
print("Number of Dimesions:", arr.ndim)


# NUMPY ARRAY INDEXING
# Index starts with 0
# array indexing is the same as accessing an array element

arr = np.array([1, 3, 5, 7, 9])
print(arr[0])
print(arr[1])
print(arr[2])
print(arr[3])
print(arr[4])

# GET 3rd and 4th element
arr = np.array([11, 33, 55, 77, 99])
print(arr[2] + arr[3])

# Accessing 2-D Array
arr = np.array([[2, 4, 6, 8], [10, 12, 14, 16]])
print("2nd element of 1st row", arr[0, 1])
print("4th element of 2nd row", arr[1, 3])
print("3rd element of 2nd row", arr[1, 2])
print("4th element of 1st row", arr[0, 3])


# Access 3-D
# To Access 3D Arrays
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print("Third Element of the second arrary of first array", arr[0, 1, 2])


# Negative Indexing

arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print("Last Element from 2nd Dim", arr[1, -1])
print("Last Element from 1st Dim", arr[0, -1])


# NUMPY ARRAY SLICING
# SLICING - Taking elements from one index to another index
# SLICE - [Start:end]

# Slice Elements from index 1 to index 5 from array

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
print(arr[1:5])
#output  - [2,3,4,5]

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
print(arr[4:])
#output - [5,6,7,8,9]

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
print(arr[0:4])
#output - [1,2,3,4]


# STEP VALUE TO DETERMINE THE STEP OF SLICING
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
print(arr[1:5:2])

# SLICING 2-D Arrays
arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(arr[1, 1:4])
#output - [7,8,9]


arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(arr[0:2, 2])
#output - [3,8]


# NUMPY DATATYPES
#string,integer, float, boolean,complex

# Check the datatype
arr = np.array([1, 2, 3, 4, 5])
arr1 = np.array([2.3, 3.5, 5.5, 7.8, 9.8])
arrstr = np.array(['ANIL', 'Kumar', 'DAROORI'])
print("The Datatype is ", arr.dtype)
print("The Datatype is", arr1.dtype)
print("The Datatype is", arrstr.dtype)


# Creating Arrays with defined datatype
arr1 = np.array([1, 2, 3, 4], dtype='S')
print(arr1)
print(arr1.dtype)


arr2 = np.array([1.1, 2.1, 3.1, 4.1], dtype='i4')
print(arr2)
print(arr2.dtype)


# Throws error
# arr3 = np.array(['1','a', 'z'],dtype='i')
# print(arr3)
# print(arr3.dtype)


# Converting Datatype

arr = np.array([2.3, 3.5, 5.5, 7.8, 9.8])
newarr = arr.astype('i')
print(newarr)
print(newarr.dtype)
#output - [2,3,5,7,9]
