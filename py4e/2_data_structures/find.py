# Escriba código usando find() y corte de cadenas (consulte la sección 6.10)
# para extraer el número al final de la línea a continuación.
# Convierta el valor extraído en un número de coma flotante e imprímalo.

text = "X-DSPAM-Confidence:    0.8475"
start = text.find('0')
end = text.find('5')
number = float(text[start : end+1])
print(number)

# Otra manera de resolver este ejercicio es la siguiente:

# text = "X-DSPAM-Confidence:    0.8475"
# start = text.find(':')
# number = text[start+4:]
# number = float(number)
# print(number)
