""" Escribir tres funciones Python que implementen una sencilla herramienta 
    de conversión de temperatura.
    Ten cuidado de escribir correctamente los nombres de los métodos. """

def celsius_to_fahrenheit(celsius):
    """ Convierte grados Celsius a Fahrenheit. """
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    """ Convierte grados Fahrenheit a Celsius. """
    return (fahrenheit - 32) * 5/9

def convert_temperature(temperature, unit):
    """ Convierte la temperatura a la unidad especificada ('C' o 'F'). """
    if unit.upper() == 'F':
        return celsius_to_fahrenheit(temperature)   # Convierte a Fahrenheit
    elif unit.upper() == 'C':
        return fahrenheit_to_celsius(temperature) # Convierte a Celsius
    else:
        raise ValueError("Unidad no válida. Usa 'C' para Celsius o 'F' para Fahrenheit.")
    
# Ejemplos de uso:
print(celsius_to_fahrenheit(0))    # Debería devolver 32.0
print(fahrenheit_to_celsius(32))   # Debería devolver 0.0
print(convert_temperature(100, 'C'))  # Debería devolver 37.77777777777778
print(convert_temperature(212, 'F'))  # Debería devolver 413.6

temperature_c = 25
temperature_f = 77

converted_f = convert_temperature(temperature_c, 'F') # Convierte 25°C a 77°F
converted_c = convert_temperature(temperature_f, 'C') # Convierte 77°F a 25°C

# Debería devolver 25°C is equal to: 77.0 °F
print(f"{temperature_c}°C is equal to {converted_f}°F")

# Debería devolver 77°F is equal to: 25.0 °C
print(f"{temperature_f}°F is equal to {converted_c}°C")