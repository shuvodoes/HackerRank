from itertools import combinations

n = int(input())
letters = input().split()
k = int(input())

combos = list(combinations(letters, k))

count_with_a = sum(1 for combo in combos if 'a' in combo)

total = len(combos)

probability = count_with_a / total

print(f"{probability:.4f}")
