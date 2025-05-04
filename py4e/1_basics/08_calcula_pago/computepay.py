# Escriba un programa para solicitar al usuario las horas y la tarifa por hora
# utilizando la entrada para calcular el pago bruto.
# El pago debe ser la tarifa normal por horas hasta 40
# y tiempo y medio por la tarifa por hora para todas las horas trabajadas por encima de las 40 horas.
# Ponga la lógica para realizar el cálculo del pago en una función
# llamada computepay() y use la función para realizar el cálculo.
# La función debe devolver un valor.
# Utilice 45 horas y una tarifa de 10,50 por hora para probar el programa
# (la paga debería ser de 498,75). Debe usar input para leer una cadena
# y float() para convertir la cadena en un número.
# No se preocupe por el error al verificar la entrada del usuario a menos que lo desee;
# puede asumir que el usuario escribe los números correctamente.
# No nombre su variable sum ni use la función sum().

def computepay(h, r):
    added = h + r
    return added

hrs = input("Enter Hours: ")
h = float(hrs)

rate = input("Enter rate: ")
r = float(rate)

if h > 40:
    sub = h * r
    sub2 = (h - 40) * (r *0.5)
    p = computepay(sub, sub2)
    print("Pay", p)
else:
    tot = h * r
    print("Pay", tot)
