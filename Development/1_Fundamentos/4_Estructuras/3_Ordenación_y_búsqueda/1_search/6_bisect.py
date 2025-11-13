import bisect

# Define a sorted list of numbers
sorted_numbers = [1, 3, 4, 7, 9]

# Insert a new number into the sorted list while maintaining order
new_number = 5
bisect.insort(sorted_numbers, new_number)

# Print the updated list
print("Updated list after insertion:", sorted_numbers)