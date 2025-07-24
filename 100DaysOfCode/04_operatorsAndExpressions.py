""" Day 4: Basic Operators and Expressions
Arithmetic Operators
Write a program to perform the following arithmetic operations using two numbers:
    Addition (+)
    Subtraction (-)
    Multiplication (*)
    Division (/)
    Floor Division (//)
    Modulus (%)
    Exponentiation (**)

Relational Operators
Write a program to compare two numbers using the following operators:
    Equal to (==)
    Not equal to (!=)
    Greater than (>)
    Less than (<)
    Greater than or equal to (>=)
    Less than or equal to (<=)

Logical Operators
Write a program that evaluates the following between 2 booleans(True or False):
    Logical AND (and)
    Logical OR (or)
    Logical NOT (not)
"""
num1 = 10
num2 = 3
# Arithmetic Operations
print("\nArithmetic Operations:")
print("Addition (10 + 3):", num1 + num2 )
print("Subtraction (10 - 3):", num1 - num2)
print("Multiplication (10 * 3):", num1 * num2)
print("Division (10 / 3):", num1 / num2)
print("Floor Division (10 // 3):", num1 // num2)
print("Modulus (10 % 3):", num1 % num2)
print("Exponentiation (10 ** 3):", num1 ** num2)

print("\nRelational Operations:")
# Relational Operations
print("Is 10 equal to 3 (10 == 3):", num1 == num2)
print("Is 10 not equal to 3 (10 != 3):", num1 != num2)
print("Is 10 greater than 3 (10 > 3):", num1 > num2)
print("Is 10 less than 3 (10 < 3):", num1 < num2)
print("Is 10 greater than or equal to 3 (10 >= 3):", num1 >= num2)
print("Is 10 less than or equal to 3 (10 <= 3):", num1 <= num2)

print("\nLogical Operations:")
# Logical Operations
true_value = True
false_value = False

print("True AND False:", true_value and false_value)
print("True AND True:", true_value or true_value)
print("False AND False:", false_value and false_value)
print("True OR False:", true_value or false_value)
print("True OR True:", true_value or true_value)
print("False OR False:", false_value or false_value)
print("Not True:", not true_value)
print("Not False:", not false_value)
