""" Day 6: Functions and Code Reusability
Functions are reusable blocks of code that make programs easier to read, debug, 
and maintain. Learn how to define, call, and use functions effectively.

Simple Function
Define and call a simple function greet_user which takes name as a parameter. 
The function should print 'Hello, name' to the console.

Default and Keyword Arguments
Update the greet_user function by adding a default value 'Guest' for the name parameter. 
When the function is called without an argument it should print 'Hello, Guest' to 
the console.

Function with Return Values
Write a function that calculates and returns the area of a rectangle. 
The function should take length and breadth as the arguments.

Variable Scope
To understand the difference between local and global variables, follow these steps:
1. Define a global variable and print its value.
2. Write a function and assign a new value to the same varible inside the function 
    and then print it.
3. Print the variable again outside the function again to observe that its value 
    didn't change.
4. Write another function that access the global variable using the global keyword 
    and then update its value.
5. Print the variable again outside the function. 
    Verify that it's value now got updated.

You'll notice that in step 3, whatever changes made inside the function in 
step 2 are not reflected but in step 5 when you use the global keyword the 
variable value gets updated. This shows how the global keyword is used to 
modify global variables from within a function.  
"""

# Simple Function
def greet_user(name):
    print(f"Hello, {name}")
greet_user("John")
print()

# Default and Keyword Arguments
def greet_user(name="Guest"):
    print(f"Hello, {name}")
greet_user()  # No argument, should print 'Hello, Guest'
greet_user("John")  # With argument, should print 'Hello, John'
print()

# Function with Return Values
def calculate_area(length, breadth):
    return length * breadth
area = calculate_area(5, 3)
print(f"The area of the rectangle is {area}.")
print()

# Variable Scope
global_var = 10
print(f"Global variable before function call: {global_var}")
def modify_variable():
    local_var = 20  # This is a local variable
    print(f"Local variable inside function: {local_var}")

modify_variable()
print(f"Global variable after function call: {global_var}")

def modify_global_variable():
    global global_var  # Declare the variable as global
    global_var = 20  # Modify the global variable
    print(f"Updated global variable inside function: {global_var}")

modify_global_variable()
print(f"Global variable after function call: {global_var}")
