""" Día 25: frecuencia de palabras
Escriba una función para contar la frecuencia de las palabras en una oración. """
def word_frequency(sentence):
    words = sentence.split()
    frequency = {}
    for word in words:
        word = word.lower().strip('.,!?;"\'()[]{}')
        if word:
            frequency[word] = frequency.get(word, 0) + 1
    return frequency

sentence_input = input("Ingrese una oración: ")
print(f"La frecuencia de palabras en la oración es: {word_frequency(sentence_input)}.")
# Ejemplo de uso
# Ingrese una oración: Hola mundo hola
# La frecuencia de palabras en la oración es: {'hola': 2, 'mundo': 1}.
# Ejemplo de uso
# Ingrese una oración: Esto es una prueba. Esto es solo una prueba!
# La frecuencia de palabras en la oración es: {'esto': 2, 'es': 2, 'una': 2, 'prueba': 2, 'solo': 1}.
# Ejemplo de uso
# Ingrese una oración: Python es genial. Python es divertido.
# La frecuencia de palabras en la oración es: {'python': 2, 'es': 2, 'genial': 1, 'divertido': 1}.