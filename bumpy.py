import numpy as np   

arr = np.array([[1, 2, 3, 4, 5]]) #1-D
print(arr)
print(type(arr)) #<class 'numpy.ndarray'>  ndarray = n-dimensional array

arr = np.array([[[[1, 2, 3, 4, 5],[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5]]]])
print(arr)

print(arr.ndim)
