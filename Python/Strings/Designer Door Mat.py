# Get input
X, M = map(int, input().split())

# Top half of the mat
for i in range(1, X, 2):
    pattern = (".|." * i).center(M, '-') 
    print(pattern)

# Center with "WELCOME"
print("WELCOME".center(M, '-'))

# Bottom half of the mat
for i in range(X-2, 0, -2):
    pattern = (".|." * i).center(M, '-')  # Create the pattern and center it within M columns
    print(pattern)
