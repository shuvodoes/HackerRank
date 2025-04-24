# Problem: Transpose and Flatten - HackerRank NumPy Challenge


# Task Description:
# You are given a 2D integer array of dimensions n x m (n rows and m columns).
# Your task is to:
#   1. Print the transpose of the array.
#   2. Print the flattened version of the array.


# Input Format:
# The first line contains two integers n and m.
# The next n lines each contain m integers.

# Output Format:
# Print two outputs:
#   - First, the transpose of the array.
#   - Second, the flattened array.

# Sample Input:
# 2 3
# 1 2 3
# 4 5 6

# Sample Output:
# [[1 4]
#  [2 5]
#  [3 6]]
# [1 2 3 4 5 6]

# Code Implementation:

import numpy as np

# Step 1: Read the shape of the array
n, m = map(int, input().split())

# Step 2: Read the 2D array input from user
arr = np.array([list(map(int, input().split())) for _ in range(n)])

# Step 3: Print the transpose of the array
print(arr.T)

# Step 4: Print the flattened version of the array
print(arr.flatten())
