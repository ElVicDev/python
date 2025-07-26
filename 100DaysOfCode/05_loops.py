""" Day 5: Conditional Statements and Loops
If-else Statements
    Write a program that takes an integer as input and checks if it's even or odd.
    Write a program that takes an age as input and determines if the person is 
    a child, teenager, adult, or senior citizen.

Nested If-else Statements
    Using nested if-else, write a program that takes three numbers as input 
    and determines the largest among them.

For Loop
    Write a program to calculate the sum of all numbers up to the given input number.

While Loop
    Write a program to calculate the factorial of a given number.
"""
# If-else Statements
# Check if a number is even or odd
number = int(input("Enter an integer: "))
if number % 2 == 0:
    print(f"{number} is even.")
else:
    print(f"{number} is odd.")

# Determine age category
age = int(input("\nEnter your age: "))
if age < 13:
    print("You are a child.")
elif age < 20:
    print("You are a teenager.")
elif age < 60:
    print("You are an adult.")
else:
    print("You are a senior citizen.")

# Nested If-else Statements
# Find the largest of three numbers
num1 = int(input("\nEnter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))

if num1 >= num2:
    if num1 >= num3:
        print(f"The largest number is {num1}.")
    else:
        print(f"The largest number is {num3}.")
else:
    if num2 >= num3:
        print(f"The largest number is {num2}.")
    else:
        print(f"The largest number is {num3}.")

# For Loop
# Calculate the sum of all numbers up to a given number
number = int(input("\nEnter a positive number to calculate the sum up to that number: "))
sum = 0
for n in range(1, number + 1):
    sum += n
print(f"The sum of all numbers up to {number} is {sum}.")

# While Loop
# Calculate the factorial of a given number
number = int(input("\nEnter a positive integer to calculate its factorial: "))
factorial = 1
while number > 1:
    factorial *= number
    number -= 1
print(f"The factorial of {number} is {factorial}.")
