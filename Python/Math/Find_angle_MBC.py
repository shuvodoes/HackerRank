"""
ABC is a right triangle, 90° at B.
Therefore, ABC = 90°

Point M is the midpoint of hypotenuse AC .

You are given the lengths AB and BC.
Your task is to find  (angle , as shown in the figure) in degrees.

Note: Round the angle to the nearest integer.

Examples:
If angle is 56.5000001°, then output 57°.
If angle is 56.4999999°, then output 56°.

"""

# Solution

from math import degrees, atan2

# Input
AB = float(input())
BC = float(input())

# Calculation
MBC = round(degrees(atan2(AB, BC)))

print((str(MBC)), chr(176), sep='')

