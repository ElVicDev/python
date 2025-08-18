""" Día 28: Palabras inversas
Reverse las palabras en una oración. """

def reverse_words(sentence):
    words = sentence.split()
    reversed_words = ' '.join(reversed(words))
    return reversed_words
sentence_input = input("Ingrese una oración: ")
reversed_sentence = reverse_words(sentence_input)
print(f'Las palabras en la oración invertida son: "{reversed_sentence}"')

# Ejemplo de uso
# Ingrese una oración: El gato duerme en la casa
# Las palabras en la oración invertida son: "casa la en duerme gato El"

# Ejemplo de uso
# Ingrese una oración: Python es divertido
# Las palabras en la oración invertida son: "divertido es Python"

# Ejemplo de uso
# Ingrese una oración: Hola mundo
# Las palabras en la oración invertida son: "mundo Hola"