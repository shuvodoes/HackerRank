# Solution
n = int(input())
A = set(map(int, input().split()))

N = int(input())

for _ in range(N):
    command = input().split()[0]
    other_set = set(map(int, input().split()))
    getattr(A, command)(other_set)

print(sum(A))
