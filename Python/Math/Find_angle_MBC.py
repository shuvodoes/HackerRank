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

import math

# Degree Symbol
DEGREE_SYMBOL = chr(176)

# Input
a = int(input())
b = int(input())

# Calculation
angle_rad = math.atan2(b, a)
angle_deg = math.degrees(angle_rad)
rounded_angle = round(angle_deg)

# Output
print(f"{rounded_angle}{DEGREE_SYMBOL}")
