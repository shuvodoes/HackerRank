"""
#HackerRank Problem: Find a string.

Problem Statement:
 In this challenge, the user enters a string and a substring. You have to print the number of times that the substring occurs in the given string.
 String traversal will take place from left to right, not from right to left.

Input Format:
 First line: The original string
 Second line: The substring 
                                     
Constraints:
 1<= len(string) <= 200
 Each character in the string is an ascii character.

Output Format:
 Output the integer number indicating the total number of occurrences of the substring in the original string.

  """
#Solution:

def count_substring(string, sub_string):
  
    count = 0 
    string_len = len(string)
    substring_len = len(sub_string)
    loop_range = string_len - substring_len + 1
    
    # Slide through the string one character at a time
    for i in range(loop_range):
        # Extract a segment of the same length as sub_string
        current_segment = string[i:i+substring_len]
        
        # If this segment matches the substring 
        if current_segment == sub_string:
            count += 1
            
    return count

if __name__ == '__main__':

    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
