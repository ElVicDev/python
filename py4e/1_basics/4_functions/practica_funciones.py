def greet(lang):
        if lang == 'es':
        	return 'Hola'
        elif lang == 'fr':
        	return 'Bonjour'
        else:
        	return 'Hello'
def live():
	print('México')
def addtwo(a, b):
	added = a + b
	return added
def name_full(n, a1, a2):
	addname = n + a1 + a2
	return addname

name = input("¿Cuál es tu Nombre?: ")

print(greet('es'), name, 'gusto en conocerte')

print('¿Dónde Vives? ')
live()
print('Me gustaría conocer')
live()
inp = input("Ahora dime cuál es tu primer apellido: ")
big = max(inp)
tiny = min(inp)
print('La letra en tu primer apellido que está al final del código ASCII es:')
print(big)
print('Y la letra en tu primer apellido que está al principio del código ASCII es:')
print(tiny)

inp2 = input("Cuál es tu segundo apellido? ")
big2 = max(inp2)
tiny2 = min(inp2)

print('La letra en tu nombre que está al final del código ASCII es:')
print(big2)
print('Y la letra en tu nombre que está al principio del código ASCII es:')
print(tiny2)

num1 = input("Ingresa un numero: ")
num1 = int(num1)
num2 = input("Ingresa otro numero: ")
num2 = int(num2)
sum = int(addtwo(num1, num2))
print('La suma de estos números que proporcionas es: ', sum)
complete = name_full(name, inp, inp2)
print('La cadena de caracteres con tu nombre es: ', complete)
print("A D I O S ! ! !")