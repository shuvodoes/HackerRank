#Solution

from itertools import permutations

S, k = input().split()
k = int(k)

perm_list = sorted(permutations(S, k))

for p in perm_list:
    print(''.join(p))
