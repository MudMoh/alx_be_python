# This script generates a multiplication table for a number provided by the user.

# Prompt the user for a number and convert the input to an integer
try:
    number = int(input("Enter a number to see its multiplication table: "))
except ValueError:
    print("Invalid input. Please enter a valid number.")
else:
    # Use a for loop to iterate from 1 to 10 and print the multiplication table
    for i in range(1, 11):
        product = number * i
        print(f"{number} * {i} = {product}")
