# Ejemplo de Escape Character usando la barra invertida \
import re
x = 'We just received $10.00 for cookies.'
y = re.findall('\\$[0-9.]+', x)  # Busca los numeros entre el 0 y el 9
                                # después del simbolo $ y si hay mas numeros despues del punto
print(y)                        # imprime ['$10.00']
