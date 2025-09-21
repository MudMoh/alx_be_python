# This script draws a square pattern of asterisks based on user input.

# Prompt the user for the size of the pattern
try:
    size = int(input("Enter the size of the pattern: "))
    
    # Check if the input is a positive integer
    if size <= 0:
        print("Please enter a positive integer.")
    else:
        # Use a while loop to handle the rows of the pattern
        row = 0
        while row < size:
            # Use a for loop to print the asterisks for each row
            for _ in range(size):
                print("*", end="")
            
            # Print a newline character after each row is completed
            print()
            
            # Increment the row counter
            row += 1

except ValueError:
    print("Invalid input. Please enter a valid positive integer.")
