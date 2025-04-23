# HackerRank Problem: Array Mathematics
# Task: Given two integer matrices A and B of size n x m,
# perform element-wise operations: addition, subtraction, multiplication,
# integer division, modulus, and power using NumPy.

import numpy as np

# Read dimensions of the arrays
n, m = map(int, input().split())

# Read array A of size n x m
A = np.array([input().split() for _ in range(n)], int)

# Read array B of size n x m
B = np.array([input().split() for _ in range(n)], int)

# Perform and print element-wise operations between arrays A and B
print(np.add(A, B))           # Element-wise addition
print(np.subtract(A, B))      # Element-wise subtraction
print(np.multiply(A, B))      # Element-wise multiplication
print(np.floor_divide(A, B))  # Element-wise integer (floor) division
print(np.mod(A, B))           # Element-wise modulus (remainder)
print(np.power(A, B))         # Element-wise power (A^B)

