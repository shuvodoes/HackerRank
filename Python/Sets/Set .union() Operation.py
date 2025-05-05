# Solution

n1 = int(input())
english = set(map(int, input().split()))

n2 = int(input())
french = set(map(int, input().split()))

union_set = english.union(french)

print(len(union_set))
