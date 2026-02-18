# Enter your code here. Read input from STDIN. Print output to STDOUT

from collections import defaultdict

# Read n and m
n, m = map(int, input().split())

# Use a defaultdict of lists to store indices
# If a word isn't in the dict, it will automatically create an empty list
group_a = defaultdict(list)

# Read Group A words and store their 1-indexed positions
for i in range(1, n + 1):
    word = input().strip()
    group_a[word].append(str(i))

# Read Group B words and check group_a
for _ in range(m):
    word_b = input().strip()
    
    if word_b in group_a:
        # Print the joined indices
        print(" ".join(group_a[word_b]))
    else:
        # Word not found in Group A
        print("-1")
