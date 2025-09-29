""" Escribir una función que calcule el diámetro de un círculo a partir de su radio.
El diámetro es el doble del radio. """

def calculate_diameter(radius: float) -> float:
    """Calcula el diámetro de un círculo dado su radio."""
    # Si el usuario envía un radio negativo, la función debe devolver -1
    if radius < 0:
        return -1
    # Si el usuario envía un radio 0, la función debe devolver 0
    if radius == 0:
        return 0
    return 2 * radius

# Ejemplos de uso
radius = 7
diameter = calculate_diameter(radius)
print(f"El diámetro de un círculo con radio {radius} es {diameter}.")

# Output:
# El diámetro de un círculo con radio 7 es 14
radius = 2.5
diameter = calculate_diameter(radius)
print(f"El diámetro de un círculo con radio {radius} es {diameter}.")

# Output:
# El diámetro de un círculo con radio 2.5 es 5.0
radius = 0
diameter = calculate_diameter(radius)
print(f"El diámetro de un círculo con radio {radius} es {diameter}.")

# Output:
# El diámetro de un círculo con radio 0 es 0
radius = -3
diameter = calculate_diameter(radius)
print(f"El diámetro de un círculo con radio {radius} es {diameter}.")

# Output:
# El diámetro de un círculo con radio -3 es -1
radius = 1000000
diameter = calculate_diameter(radius)
print(f"El diámetro de un círculo con radio {radius} es {diameter}.")
# Output:
# El diámetro de un círculo con radio 1000000 es 2000000