"""
Task:
You are given a partial code that is used for generating the HackerRank Logo of variable thickness.
Your task is to replace the blank (______) with rjust, ljust or center.

Input Format:
A single line containing the thickness value for the logo.

Constraints:
The thickness must be an odd number.

"""


# Solution

inp = int(input()) #This must be an odd number
c = 'H'
for i in range(inp):
    print((c*i).rjust(inp-1)+c+(c*i).ljust(inp-1))

for i in range(inp+1):  print((c*inp).center(inp*2)+(c*inp).center(inp*6))

for i in range((inp+1)//2):
    print((c*inp*5).center(inp*6))    

for i in range(inp+1): print((c*inp).center(inp*2)+(c*inp).center(inp*6))    

for i in range(inp):  print(((c*(inp-i-1)).rjust(inp)+c+(c*(inp-i-1)).ljust(inp)).rjust(inp*6))
  
# Sample Input:
# 5

# Sample Output 0:
#     H    
#    HHH   
#   HHHHH  
#  HHHHHHH 
# HHHHHHHHH
#   HHHHH               HHHHH             
#   HHHHH               HHHHH             
#   HHHHH               HHHHH             
#   HHHHH               HHHHH             
#   HHHHH               HHHHH             
#   HHHHH               HHHHH             
#   HHHHHHHHHHHHHHHHHHHHHHHHH   
#   HHHHHHHHHHHHHHHHHHHHHHHHH   
#   HHHHHHHHHHHHHHHHHHHHHHHHH   
#   HHHHH               HHHHH             
#   HHHHH               HHHHH             
#   HHHHH               HHHHH             
#   HHHHH               HHHHH             
#   HHHHH               HHHHH             
#   HHHHH               HHHHH             
#                      HHHHHHHHH   
#                       HHHHHHH  
#                        HHHHH   
#                         HHH    
#                          H  


