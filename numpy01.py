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


# Accessing the Array Index
# Initial Array
arr = np.array([[-1, 2, 0, 4],
               [2, 3, 5, 6],
               [4, 5, 8, 9],
               [1, 2, 3, 4]])
print("Initial Array")
print(arr)

# Print of Range of Array using slicing method
sliced_arr = arr[:2, ::2]
print("Sliced Array", sliced_arr)

# Printing elements at specific indices
Index_arr = arr[[1, 1, 0, 3],
                [3, 2, 1, 0]]
print("\nElements at indices (1,2),(1,3)", Index_arr)


# BASIC ARRAY OPERATIONS
# MATHEMATICAL, UNARY and BINARY OPERATIONS

# DEFINING ARRAY NO.1
a = np.array([[1, 2],
              [3, 4]])

# DEFINING ARRAY NO.2
b = np.array([[4, 5],
              [6, 7]])

# Adding 1 to every element
print("Adding 1 to every element:", a+1)
print("Adding 2 to every element:", a+2)


# Subtract 1 from every element
print("Subtract 1 from every element:", b-1)
print("subtract 2 from every element:", b-2)


# Sum of all array elements
print("Sum of all array elements:", a.sum())


# Adding Two Arrays
# Binary Operations
print("\n Array Sum", a+b)


# Square each element
print("Square of each element:", a**2)

# Transpose of array
Transpose = np.array([[1, 2, 3],
                      [4, 5, 6],
                      [7, 8, 9]])
print("Original array:", Transpose)
print("Transpose of Array:", Transpose.T)


# UNARY OPERATORS
# Largest element in array

arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("Largest Element in array:", arr.max())
print("Smallest Element in array:", arr.min())
print("Row wise array largest element:", arr.max(axis=1))
print("Row wise array smallest element:", arr.min(axis=0))

# Cumulative sum of each row
print("Cumulative sum of each array:", arr.cumsum(axis=1))


# Square Root of array values
d = np.array([[1, 9, 16], [25, 36, 49]])
print("Square Root of each element:", np.sqrt(d))

# Array elements in sorted order
sort_array = np.array([[20, 14, 3], [1, 50, 22], [31, 12, 18]])
print("Array in sorted order:", np.sort(sort_array, axis=None))
print("Array in sorted order - row wise:", np.sort(sort_array, axis=1))


# STACKING - SEVERAL ARRAYS STACKED TOGETHER

arr1 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
arr2 = np.array([[11, 12, 13], [14, 15, 16], [17, 18, 19]])
print("Vertical Stacking:", np.vstack((arr1, arr2)))
print("Horizontal Stacking:", np.hstack((arr1, arr2)))

# Concatenation of two arrays

print("Concatenation of arrays:", np.concatenate((a, b), 1))


# Splitting Array

a = np.array([[1, 3, 5, 7, 9, 11],
              [2, 4, 6, 8, 10, 12]])

# horizontal splitting
print("Splitting along horizontal axis into 2 parts:\n", np.hsplit(a, 2))
print("Splitting along Vertical axis into 2 parts:\n", np.vsplit(a, 2))


# Numpy DataType Object
x = np.array([1, 2, 3])
print("Integer Datatype")
print(x.dtype)

y = np.array([1.0, 2.0, 3.0])
print("Float Datatype")
print(y.dtype)


# NUMPY STRING OPERATIONS
# numpy.lower() function - convert to lowercase
print("Converting into LOWER CASE")
print(np.char.lower(["DAROORI ANILKUMAR"]))

# numpy.upper() function - convert to uppercase
print("Converting into UPPER CASE")
print(np.char.upper(["daroori pinky"]))


# SPLIT FUNCTION - Split based specified seperator
print(np.char.split('ANIL KUMAR'))


# NUMPY JOIN
# numpy.join Function()
print(np.char.join('DAROOR', 'IANILKUMAR'))

# Remove all leading and trailing spaces
print("STRIP FUNCTION")
print(np.char.strip('ANIL '))


# NUMPY COUNT
# numpy.count Function()
a = np.array(['ANIL', 'VIRAT', 'RAHUL'])
print("COUNT OF SUBSTRING IN EACH WORD")
print(np.char.count(a, 'A'))


# NUMPY RFIND
# numpy.rfind() function

a = np.array(['ANIL', 'VIRAT', 'RAHUL'])
print(np.char.rfind(a, 'A'))


# NUMPY NUMERIC
# numpy.isnumeric() Function - check all characters - TRUE, else false
print(np.char.isnumeric('ANILKUMAR189'))


# numpy.equal
a = np.char.equal('ANIL', 'KUMAR')
print(a)


# LINEAR ALGEBRA
A = np.array([[6, 1, 1],
             [4, -2, 5],
             [2, 8, 7]])
print("LINEAR ALGEBRA:", A)


# RANK OF THE MATRIX
print("RANK of A:", np.linalg.matrix_rank(A))

# Trace of Matrix
print("Trace of A:", np.trace(A))

# Determinant of a Matrix
print("Determinant of A:", np.linalg.det(A))


# Inverse of a Matrix
print("Inverse of A:", np.linalg.inv(A))


# NUMPY SORTING
# numpy.sort() - function returns sorted copy of array

# sort along the first axis
a = np.array([[12, 15], [10, 1]])
arr1 = np.sort(a, axis=0)
print("Along first axis:", arr1)


# sort along the last axis
a = np.array([[10, 15], [12, 1]])
arr2 = np.sort(a, axis=-1)
print("\nAlong last axis : \n", arr2)


# numpy.argsort()
# This function returns the indices that would sort an array

a = np.array([9, 3, 1, 7, 6, 4, 2, 5])
print("Original Array:", a)


# NUMPY UNIVERSAL FUNCTIONS
# TRIGNOMETRY FUNCTIONS

# Create an array of angles
angles = np.array([0, 30, 45, 60, 90, 180])

