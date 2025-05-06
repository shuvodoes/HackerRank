# Solution

n = int(input())
eng_students = set(map(int, input().split()))

m = int(input())
french_students = set(map(int, input().split()))

print(len(eng_students.intersection(french_students)))
