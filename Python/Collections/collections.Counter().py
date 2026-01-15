# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter

# Read number of shoes
n = int(input())

# Read the list of shoe sizes
shoe_sizes = list(map(int, input().split()))

# Create a Counter to track how many shoes of each size are available
inventory = Counter(shoe_sizes)

# Read number of customers
num_customers = int(input())

# Initialize total money earned
total_earned = 0

# Process each customer's request
for _ in range(num_customers):
    size, price = map(int, input().split())
    
    # Check if the desired shoe size is available
    if inventory[size] > 0:
        total_earned += price   # Add the price to total money earned
        inventory[size] -= 1    # Decrease the count of that shoe size

# Print the total money earned
print(total_earned)

