# Solution

m = int(input())
a = set(map(int, input().split()))

n = int(input())
b = set(map(int, input().split()))

s_dif =b.symmetric_difference(a)
 
for num in sorted(s_dif):
    print(num)
