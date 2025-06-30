from itertools import combinations_with_replacement

s, r = input().split()
r = int(r)

s = ''.join(sorted(s))

for combo in combinations_with_replacement(s, r):
    print(''.join(combo))
