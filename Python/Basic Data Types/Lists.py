# Question Type: Python Basic - List Operations
# Task: Perform a series of list operations based on given commands

if __name__ == '__main__':
    N = int(input())  # Read the number of commands
    my_list = []      # Initialize an empty list

    for _ in range(N):
        command = input().split()   # Split the command into parts
        cm = command[0]             # First part is the command name
        args = command[1:]          # Remaining parts are arguments

        # Execute the corresponding list operation
        if cm == "insert":
            # Insert value at specified index: insert(index, value)
            my_list.insert(int(args[0]), int(args[1]))
        elif cm == "print":
            # Print the current state of the list
            print(my_list)
        elif cm == "remove":
            # Remove the first occurrence of the specified value
            my_list.remove(int(args[0]))
        elif cm == "append":
            # Append value to the end of the list
            my_list.append(int(args[0]))
        elif cm == "sort":
            # Sort the list in ascending order
            my_list.sort()
        elif cm == "pop":
            # Remove the last item from the list
            my_list.pop()
        elif cm == "reverse":
            # Reverse the list
            my_list.reverse()
