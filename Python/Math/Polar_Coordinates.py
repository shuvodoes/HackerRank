"""
Task
You are given a complex number z . Your task is to convert it to polar coordinates.

Input Format
A single line containing the complex number . Note: complex() function can be used in python to convert the input as a complex number.

Constraints
Given number is a valid complex number

Output two lines:
The first line should contain the value of r .
The second line should contain the value of phi.

"""

# Solution

# Import cmath module
import cmath

# Read the input and converted to a complex number
z = complex(input().strip())

# Calculate the modulus
r = abs(z)

# Calculate the phase (phi)
phi = cmath.phase(z)


print(r)
print(phi)
