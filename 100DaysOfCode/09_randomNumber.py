""" Día 9: Generador de números aleatorios
1. Escriba un programa que genera un número aleatorio. 
2. Escriba un programa que genera un número aleatorio entre 2 enteros
"""
import random
# Generar un número aleatorio entre 0 y 100
random_number = random.randint(0, 100)
print("Random number between 0 and 100:", random_number)

# Generar un número aleatorio entre dos enteros
def generate_random_number(min_value, max_value):
    return random.randint(min_value, max_value)
# Ejemplo de uso
min_value = 10
max_value = 50
random_number_range = generate_random_number(min_value, max_value)
print(f"Random number between {min_value} and {max_value}:", random_number_range)
# Generar un número aleatorio entre 1 y 6 (simulando un dado)
dice_roll = random.randint(1, 6)
print("Dice roll (random number between 1 and 6):", dice_roll)
# Generar un número aleatorio de punto flotante entre 0 y 1
random_float = random.random()
print("Random float between 0 and 1:", random_float)
# Generar un número aleatorio de punto flotante entre dos valores
def generate_random_float(min_value, max_value):
    return random.uniform(min_value, max_value)
# Ejemplo de uso
min_float = 1.5
max_float = 5.5
random_float_range = generate_random_float(min_float, max_float)
print(f"Random float between {min_float} and {max_float}:", random_float_range)
# Generar un número aleatorio de punto flotante entre 0 y 10
random_float_0_10 = random.uniform(0, 10)
print("Random float between 0 and 10:", random_float_0_10)
# Generar un número aleatorio de punto flotante entre 1 y 100
random_float_1_100 = random.uniform(1, 100)
print("Random float between 1 and 100:", random_float_1_100)
# Generar un número aleatorio de punto flotante entre -10 y 10
random_float_neg10_10 = random.uniform(-10, 10)
print("Random float between -10 and 10:", random_float_neg10_10)
# Generar un número aleatorio de punto flotante entre -100 y 100
random_float_neg100_100 = random.uniform(-100, 100)
print("Random float between -100 and 100:", random_float_neg100_100)
# Generar un número aleatorio de punto flotante entre 0 y 1 con precisión de 2 decimales
random_float_0_1_precise = round(random.uniform(0, 1), 2)
print("Random float between 0 and 1 with 2 decimal places:", random_float_0_1_precise)
# Generar un número aleatorio de punto flotante entre 0 y 100 con precisión de 2 decimales
random_float_0_100_precise = round(random.uniform(0, 100), 2)
print("Random float between 0 and 100 with 2 decimal places:", random_float_0_100_precise)
# Generar un número aleatorio de punto flotante entre 1 y 10 con precisión de 2 decimales
random_float_1_10_precise = round(random.uniform(1, 10), 2)
print("Random float between 1 and 10 with 2 decimal places:", random_float_1_10_precise)
# Generar un número aleatorio de punto flotante entre -1 y 1 con precisión de 2 decimales
random_float_neg1_1_precise = round(random.uniform(-1, 1), 2)
print("Random float between -1 and 1 with 2 decimal places:", random_float_neg1_1_precise)
# Generar un número aleatorio de punto flotante entre -50 y 50 con precisión de 2 decimales
random_float_neg50_50_precise = round(random.uniform(-50, 50), 2)
print("Random float between -50 and 50 with 2 decimal places:", random_float_neg50_50_precise)
# Generar un número aleatorio de punto flotante entre -1000 y 1000
random_float_neg1000_1000_precise = round(random.uniform(-1000, 1000), 2)
print("Random float between -1000 and 1000 with 2 decimal places:", random_float_neg1000_1000_precise)
# Generar un número aleatorio de punto flotante entre 0 y 1000
random_float_0_1000_precise = round(random.uniform(0, 1000), 2)
print("Random float between 0 and 1000 with 2 decimal places:", random_float_0_1000_precise)
