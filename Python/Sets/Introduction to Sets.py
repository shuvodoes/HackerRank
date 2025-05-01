# Introduction to Sets (Hackerrank)

# Solution 

def average(array):
    # your code goes here
    sets= set(array)
    average = sum(sets)/len(sets)
    return average
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
