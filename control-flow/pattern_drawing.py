# pattern_drawing.py

# Prompt user for pattern size
size = int(input("Enter the size of the pattern: "))

# Initialize row counter
row = 0

# Use while loop to go through rows
while row < size:
    # Use for loop to print asterisks in each row
    for col in range(size):
        print("*", end="")
    # Move to the next line after finishing one row
    print()
    row += 1
