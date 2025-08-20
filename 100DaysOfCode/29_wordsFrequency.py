""" Día 29: frecuencia de palabras
Cree un diccionario de palabras y sus frecuencias. """

def word_frequency(sentence):
    words = sentence.split()
    frequency = {}
    for word in words:
        word = word.lower()
        frequency[word] = frequency.get(word, 0) + 1
    return frequency
sentence_input = input("Ingrese una oración: ")
frequency_dict = word_frequency(sentence_input)
print("Frecuencia de palabras:", frequency_dict)

# Ejemplo de uso
# Ingrese una oración: El gato duerme en la casa y el gato juega
# Frecuencia de palabras: {'el': 2, 'gato': 2, 'duerme': 1, 'en': 1, 'la': 1, 'casa': 1, 'y': 1, 'juega': 1}

# Ejemplo de uso
# Ingrese una oración: Python es divertido y Python es poderoso
# Frecuencia de palabras: {'python': 2, 'es': 2, 'divertido': 1, 'y': 1, 'poderoso': 1}

# Ejemplo de uso
# Ingrese una oración: Hola mundo hola
# Frecuencia de palabras: {'hola': 2, 'mundo': 1}