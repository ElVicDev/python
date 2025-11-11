# Define a list of numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Create a new list with only even numbers from the original list
even_numbers = [num for num in numbers if num % 2 == 0]

# Print the new list of even numbers
print("Even numbers:", even_numbers)