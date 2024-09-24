import numpy as np

ok= np.array([1, 2, 3])
print(ok)  
np.zeros((2, 3))  # 2x3 array of zeros
np.ones((2, 3))   # 2x3 array of ones
np.random.rand(2, 3)  # 2x3 array of random floats
np.arange(0, 10, 2)   # Array with values from 0 to 9 with a step of 2

arr = np.array([[1, 2, 3], [4, 5, 6]])
print(arr.shape)  # Output: (2, 3)
print(arr.size)   # Output: 6
print(arr.dtype)  # Output: int64
print(arr.ndim)   # Output: 2

arr = np.array([1, 2, 3, 4, 5])
print(arr[1:3])  # Output: [2 3]
arr2d = np.array([[1, 2], [3, 4], [5, 6]])
print(arr2d[1:, :])  # Output: [[3 4] [5 6]]

arr = np.array([1, 2, 3])
print(arr + 2)    # Output: [3 4 5]
print(arr * 3)    # Output: [3 6 9]

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
print(arr1 + arr2)  # Output: [5 7 9]

arr = np.array([1, 2, 3])
matrix = np.array([[10], [20], [30]])
print(arr + matrix)
# Output:
# [[11 12 13]
#  [21 22 23]
#  [31 32 33]]
arr = np.array([1, 2, 3, 4])
print(np.sum(arr))      # Output: 10
print(np.mean(arr))     # Output: 2.5
print(np.std(arr))      # Output: 1.11803

arr1 = np.array([1, 2])
arr2 = np.array([3, 4])
print(np.dot(arr1, arr2))  # Output: 11

arr = np.array([1, 2, 3, 4])
print(np.sum(arr))      # Output: 10
print(np.mean(arr))     # Output: 2.5
print(np.std(arr))      # Output: 1.11803

arr1 = np.array([1, 2])
arr2 = np.array([3, 4])
print(np.dot(arr1, arr2))  # Output: 11

matrix = np.array([[1, 2], [3, 4]])
print(np.linalg.inv(matrix))  # Inverse of the matrix

np.random.seed(42)  # Set seed for reproducibility
print(np.random.rand(3, 2))  # 3x2 array of random floats
