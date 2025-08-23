""" Día 31: Fusionar diccionarios.
Fusionar dos diccionarios. """

def merge_dictionaries(dict1, dict2):
    merged_dict = dict1.copy()  # Hacer una copia del primer diccionario
    merged_dict.update(dict2)   # Actualizar con el segundo diccionario
    return merged_dict
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
merged = merge_dictionaries(dict1, dict2)
print("Diccionario fusionado:", merged)

# Ejemplo de uso
# Diccionario fusionado: {'a': 1, 'b': 3, 'c': 4}

# Ejemplo de uso
# Diccionario fusionado: {'x': 10, 'y': 20, 'z': 30}

# Ejemplo de uso
# Diccionario fusionado: {'key1': 'value1', 'key2': 'new_value2', 'key3': 'value3'}