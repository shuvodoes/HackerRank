# HackerRank/Numpy Challenge: Convert input list to a NumPy array of floats and reverse it

import numpy as numpy

def arrays(arr):
    """
    Converts a list of strings (numbers) into a NumPy array of floats,
    and returns the reversed array.

    Parameters:
    arr (list): List of string representations of numbers.

    Returns:
    numpy.ndarray: Reversed NumPy array of floats.
    """
    ar = numpy.array(arr, dtype=float)[::-1]  # Convert to float array and reverse it
    return ar

# Read input as a space-separated string, split into list
arr = input().strip().split(' ')
result = arrays(arr)

# Print the resulting reversed NumPy array
print(result)
