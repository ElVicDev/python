# Escriba un programa para solicitar al usuario las horas y la tarifa por hora
# utilizando la entrada para calcular el pago bruto.
# Pague la tarifa por hora por las horas hasta 40
# y 1,5 veces la tarifa por hora por todas las horas trabajadas
# por encima de las 40 horas.
# Utilice 45 horas y una tarifa de 10,50 por hora para probar el programa
# (la paga debería ser de 498,75).
# Debe usar input para leer una cadena y float() para convertir
# la cadena en un número.
# No se preocupe por el error al verificar la entrada del usuario;
# suponga que el usuario escribe los números correctamente.

print("Enter Hours:")
hrs = input()
h = float(hrs)
print("Enter rate:")
rate = input()
r = float(rate)
if h > 40:
    sub = h * r
    sub2 = (h - 40) * (r *0.5)
    tot = sub + sub2
else:
    tot = h * r
print("Pay: ",tot)
