# Problem: String Mutations (HackerRank Problem)

# Task:
# Read a given string, change the character at a given index, and print the modified string.

# Function to mutate the string
def mutate_string(string, position, character):
    # Replace the character at the given position
    # Strings are immutable, so we slice and create a new string
    return string[:position] + character + string[position+1:]

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    
    print(s_new)
