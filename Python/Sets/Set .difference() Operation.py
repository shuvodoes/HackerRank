# Solution

eng = int(input())
eng_set = set(map(int,input().split()))
fra = int(input())
fra_set = set(map(int,input().split()))

difference_s = eng_set.difference(fra_set)

print(len(difference_s))
