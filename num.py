import numpy as np
# np.random.seed(0)
# # print(np.random.rand(2,12,10))

# import pandas as pd
# df = pd.read_csv('out.csv')

# print(type(df))

# print(df['Roll_number'])

# import numpy as np

# arr = np.array([7,7,7,7,3,2,4,5,6,332,234])

# x = np.searchsorted(arr, 7,side='right')

# print(x)




# Check whether a Numpy array contains a specified row
# Arr = [[1,2,3,4,5], [6,7,8,9,10], [11,12,13,14,15], [16,17,18,19,20]]

# arr = np.array(Arr)
# print(arr)
# print(arr.tolist())



# How to Remove rows in Numpy Array that contains non-numeric value
# n = np.array([[10.5, 22.5, 3.8],
#                   [np.nan, np.nan, np.nan]])

# print(n)
# c = n[~np.isnan(n).any(axis=1)]
# print(c)



#Remove single-dimensional entries from the shape of an array
#remove unnessary dimension
# np.squeeze(arr,axis =)

# n = np.array([[[10,4]],[[1,4]]])

# print(np.squeeze(n))



#Find the number of occurrences of a sequence 
#how many time this sequence is occurrer

# arr = np.array([[2, 8, 9, 4], 
#                    [9, 4, 9, 4],
#                    [4, 5, 9, 7],
#                    [2, 9, 4, 3]])

# o = repr(arr).count('2, 8, 9, 4')
# # print(type(repr(arr)))
# print(o)



#Most Frequency value in numpy array:

# x = np.array([1,2,3,4,5,1,2,1,1,1])
# print(np.bincount(x).argmax())


#Iterate over two arrays simultaneously using nditer
# num_1d = np.arange(5)
# print("One dimensional array:")
# print(num_1d)

# num_2d = np.arange(10).reshape(2,5)
# print("\nTwo dimensional array:")
# print(num_2d)

# for a, b in np.nditer([num_1d, num_2d]):
#     print(a,b)



#Hot to build an array of all  combinations of two Numpy arrays

# arr1 = np.array(np.arange(5))
# arr2 = np.array(np.arange(2,6))
# print(arr2)

# print(np.array(np.meshgrid(arr1,arr2)))
# res = np.array(np.meshgrid(arr1,arr2)).T.reshape(2,-1)
# print(res)



#How to add a border around a Numpy array
# a = np.ones((2,2))
# print(a)

# n = np.pad(a,pad_width=1)
# print(n)



#How to compare two Numpy arrays

# n_array = np.array([[1, 2], [3, 4]])
# another_array = np.array([[1, 2], [3, 4]])

# print(np.array_equal(n_array, another_array))

# a = np.array([101, 99, 87])
# b = np.array([897, 97, 111])

# print("Array a: ", a)
# print("Array b: ", b)

# print("a > b")
# print(np.greater(n_array, another_array))

# print("a >= b")
# print(np.greater_equal(a, b))

# print("a < b")
# print(np.less(a, b))

# print("a <= b")
# print(np.less_equal(a, b))



#how to check specified element is present in array 
# n = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# print(5 in n)



#How to get all 2D Diagonals of a 3D Numpy Array
# arr = np.array([[[1, 2, 3], 
#                 [4, 5, 6]],


#                 [[7, 8, 9],
#                 [10, 11, 12]],

#                 [[13, 14, 15],
#                 [16, 17, 18]]])
# diagonals = np.diagonal(arr, axis2=0, axis1=1)
# print(diagonals)



#flatten a Matrix in python using Numpy
#simply convert 2D array to 1D array

# a = np.array([[[1, 2, 3], [4, 5, 6], [7, 8, 9]]])

# print(a.flatten())



#numpy.moveaxis() funcation
# arr = np.array([[[1, 2], [3, 4]], [[5, 6],[7,8]]])
# print(arr)
# moveaxis = np.moveaxis(arr,0,1)
# print(moveaxis[0][1][0])
# print(moveaxis)



#numpy.swapaxes() function
# arr = np.array([[[1, 2, 3], [4, 5, 6]]])
# print(arr)
# swapaxes = np.swapaxes(arr, 0, 2)
# print(swapaxes)
# print(swapaxes.shape)



#numpy count_nonzero() method
# arr = np.array([[1, 2, 0], [4, 0, 6], [7, 8, 9]])
# print(np.count_nonzero(arr))



#How to find Numpy array size()fucation
# a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# print(np.size(a,0))



#numpay.trim_zeros() function
# arr = np.array([0, 1, 2, 3, 0, 0])
# trimmed_arr = np.trim_zeros(arr)
# trimmed_arr_with_left = np.trim_zeros(arr, 'f')  # Trim from the front
# trimmed_arr_with_right = np.trim_zeros(arr, 'b')  # Trim from the back
# print(trimmed_arr)



#change the Data Type of a Numpy Array
# import numpy as np
# # Create a numpy array
# arr = np.array([10, 20, 30, 40, 50])
# # Print the array
# print(arr)
# # change the dtype to 'float64'
# arr = arr.astype('float64')
# print(arr)

# # print the data type
# print(arr.dtype)



#How to Reverse a numpy array
# a = np.array([1, 2, 3, 4, 5])
# # Reverse the array
# b = np.flip(a)
# print(b)
# print(a[::-1])

# print(np.flipud(a))



#How to make a Numpy array only read-only
# arr = np.array([1, 2, 3, 4, 5])
# arr.flags.writeable = False


