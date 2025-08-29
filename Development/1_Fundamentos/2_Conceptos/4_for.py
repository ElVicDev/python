""" Crear un bucle for: Utilice la función range() para generar la 
    secuencia de números. 
    Recuerde que range(max_value + 1) incluirá max_value en el bucle.

Comprueba la divisibilidad: 
    Dentro del bucle for, utilice una sentencia if para comprobar 
    si el número actual es divisible entre 3 y 4. 
    Para ello, utilice el operador módulo (%). 
    Para ello, utilice el operador de módulo (%) para encontrar el 
    resto al dividir por 3, y de nuevo al dividir por 4. 
    Si ambos restos son 0, utilice print() para mostrar el número. """

max_value = 50
for num in range(max_value + 1):
    if num % 3 == 0 and num % 4 == 0:
        print(num)

# Salida esperada: 0, 12, 24, 36, 48