""" Día 14: Año bisiesto
Escriba un programa que verifique si un año de entrada determinado 
es un año bisiesto o no """

year = int(input("Ingrese un año: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} es un año bisiesto.")
else:
    print(f"{year} no es un año bisiesto.")
