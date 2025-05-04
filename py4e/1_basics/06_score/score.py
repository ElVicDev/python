# Escriba un programa para solicitar una puntuación entre 0,0 y 1,0.
# Si la puntuación está fuera de rango, imprime un error.
# Si la puntuación está entre 0,0 y 1,0,
# imprima una calificación utilizando la siguiente tabla:
# Calificación de puntuación
# >= 0,9 A
# >= 0,8B
# >= 0.7C
# >= 0,6D
# < 0,6 F
# Si el usuario ingresa un valor fuera de rango,
# imprime un mensaje de error adecuado y sale.
# Para la prueba, introduzca una puntuación de 0,85.

score = input("Enter Score: ")
try:
    s = float(score)
except:
    print("ERROR! Please enter score between 0.0 to 1.0)")
    quit()
if s >= 0.9:
    print("A")
    quit()
elif s >= 0.8:
    print("B")
    quit()
elif s >= 0.7:
    print("C")
    quit()
elif s >= 0.6:
    print("D")
    quit()
elif s < 0.6:
    print("f")
    quit()
