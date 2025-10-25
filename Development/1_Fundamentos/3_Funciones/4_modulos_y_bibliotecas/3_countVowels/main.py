""" Importa el módulo string_utils. 
    Esto te permitirá utilizar la función que definiste en string_utils.py """

import string_utils

sentence = "This is a test sentence to count vowels."
vowel_count = string_utils.count_vowels(sentence)
print("Number of vowels:", vowel_count)

""" Resultados esperados:
El programa imprimirá el número de vocales en la oración dada. """
# Expected output: Number of vowels: 12