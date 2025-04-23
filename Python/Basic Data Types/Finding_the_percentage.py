# Problem: Finding the Percentage
# Task: Calculate and print the average score for a given student,
# formatted to 2 decimal places.

if __name__ == '__main__':
    # Read the number of student records
    n = int(input())
    
    # Dictionary to store student names and their list of scores
    student_marks = {}

    # Loop to read each student's name and scores
    for _ in range(n):
        name, *line = input().split()  # First value is name, rest are scores
        scores = list(map(float, line))  # Convert score strings to float
        student_marks[name] = scores  # Add entry to dictionary

# Read the student name to query
query_name = input()

# Get the marks list for that student
marks = student_marks[query_name]

# Calculate average score
average = sum(marks) / len(marks)

# Print the result rounded to 2 decimal places
print(f"{average:.2f}")
