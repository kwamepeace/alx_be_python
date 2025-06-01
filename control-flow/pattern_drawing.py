# pattern_drawing.py

# Prompt user for pattern size
while True:
    try:
        size_input = input("Enter the size of the pattern: ")
        pattern_size = int(size_input)
        if pattern_size > 0:
            break  # Exit loop if a positive integer is entered
        else:
            print("Please enter a positive integer.")
    except ValueError:
        print("Invalid input. Please enter a whole number.")

# Draw the pattern
row_count = 0
while row_count < pattern_size:
    # Inner loop for printing asterisks in a single row
    for _ in range(pattern_size):
        print("*", end="")

    # After printing all asterisks for the current row, print a newline
    print()

    # Increment the row counter
    row_count += 1