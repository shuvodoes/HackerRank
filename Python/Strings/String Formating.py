"""
Given an integer, n, print the following values for each integer  from  to :
 Decimal
 Octal
 Hexadecimal (capitalized)
 Binary
 
"""

# Solution:

def print_formatted(number):
    width = len(bin(number)) - 2  # subtract 2 to exclude '0b' prefix
    for i in range(1, number + 1):
        decimal = str(i)
        octal = oct(i)[2:]
        hexadecimal = hex(i)[2:].upper()
        binary = bin(i)[2:]
        print(f"{decimal.rjust(width)} {octal.rjust(width)} {hexadecimal.rjust(width)} {binary.rjust(width)}")

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
