# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

n = int(input())

for _ in range(n):
    s = input()

    try:
        re.compile(s)

        if '++' in s or '*+' in s or '?+' in s or '+*' in s or '??' in s:
            print("False")
        else:
            print("True")

    except re.error:
        print("False")
