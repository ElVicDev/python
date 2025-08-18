""" Día 27: Palabra más larga
Encuentra la palabra más larga en una oración. """

def longest_word(sentence):
    words = sentence.split()
    longest = max(words, key=len)
    return longest
sentence_input = input("Ingrese una oración: ")
longest = longest_word(sentence_input)
print(f'La palabra más larga en la oración es: "{longest}"')

# Ejemplo de uso
# Ingrese una oración: El perro corre rápidamente por el parque
# La palabra más larga en la oración es: "rápidamente"

# Ejemplo de uso
# Ingrese una oración: Python es un lenguaje de programación poderoso
# La palabra más larga en la oración es: "programación"

# Ejemplo de uso
# Ingrese una oración: Hola mundo
# La palabra más larga en la oración es: "mundo"