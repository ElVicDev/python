"""  Basic Input and Output:
Write a program that reads a single input from the user and prints it to the console. 
For example, if the user enters their name, the program should output: 
    ""Hello, {name}""

Handling Different Data Types:
Extend the program to read and print different types of inputs. 
Ensure the inputs are properly converted to their respective types and then printed. 
The program should ask the user to enter:
    A string
    An integer
    A floating-point number
"""
name = input("Enter your name: ")  # Read a string input
print(f"Hello, {name}")
age = int(input("Enter your age: "))  # Read an integer input
height = float(input("Enter your height: "))  # Read a floating-point number input
print("\nYou entered:")
print("Name:", name)
print("Age:", age)
print("Height:", height)

print("\nData Types:")
print("Name is of type:", type(name))
print("Age is of type:", type(age))
print("Height is of type:", type(height))