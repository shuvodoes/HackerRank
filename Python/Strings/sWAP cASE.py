# HackerRank Problem: Swap Case (String Manipulation)
# Problem Type: Basic Data Types / Strings
# Task: Swap the case of each character in a given string.

# Solution 1
def swap_case(s):
    # Initialize an empty string to store the result
    result = ''
    
    # Iterate through each character in the input string
    for char in s:
        if char.isupper():
            # Convert uppercase character to lowercase
            result += char.lower()
        elif char.islower():
            # Convert lowercase character to uppercase
            result += char.upper()
        else:
            # Keep non-alphabetic characters unchanged
            result += char
    
    # Return the final string with swapped cases
    return result

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)



# Solution 2
# Task: Swap the case of each character in a given string using the built-in method.

def swap_case(s):
    # Use Python's built-in string method to swap cases directly
    return s.swapcase()

if __name__ == '__main__':
    # Read input from the user
    s = input()
    
    # Call the function to swap case
    result = swap_case(s)
    
    # Output the result
    print(result)
