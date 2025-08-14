""" Día 24: Palabras a la oración.
Escriba una función para convertir una lista de palabras en una oración. """
def words_to_sentence(words):
    if not words:
        return ""
    return ' '.join(words).strip().capitalize() + '.'

words_input = input("Ingrese una lista de palabras separadas por comas: ")
word_list = [word.strip() for word in words_input.split(",")]
print(f"La oración formada por {word_list} es: '{words_to_sentence(word_list)}'.")
# Ejemplo de uso
# Ingrese una lista de palabras separadas por comas: hola,mundo,esto,es,python
# La oración formada por ['hola', 'mundo', 'esto', 'es', 'python'] es: 'Hola mundo esto es python.'.

# Ejemplo de uso
# Ingrese una lista de palabras separadas por comas:  ,  ,   , 
# La oración formada por ['', '', '', ''] es: ''.

# Ejemplo de uso
# Ingrese una lista de palabras separadas por comas: python,es,genial
# La oración formada por ['python', 'es', 'genial'] es: 'Python es genial.'.