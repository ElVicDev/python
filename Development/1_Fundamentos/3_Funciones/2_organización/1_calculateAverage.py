""" Calcular el promedio """

def calculate_average(numbers):
    total = 0  # Local variable
    count = len(numbers)  # Local variable
    for num in numbers:
        total += num
    average = total / count
    return average

print(calculate_average([2, 5, 4, 1]))