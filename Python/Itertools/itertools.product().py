# Solution

from itertools import product

A = list(map(int, input().split()))
B = list(map(int, input().split()))

result = product(A, B)

for item in result:
    print(item, end=' ')
