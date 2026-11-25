# Enter your code here. Read input from STDIN. Print output to STDOUT


from collections import namedtuple

n = int(input())
columns = input().split()

Student = namedtuple('Student', columns)

total = 0

for _ in range(n):
    data = input().split()
    student = Student(*data)
    total += int(student.MARKS)

print(f"{total / n:.2f}")
