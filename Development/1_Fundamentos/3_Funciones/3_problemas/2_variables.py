# Argumentos con palabras clave
""" 
Al llamar a una función con parámetros opcionales, puede especificar 
explícitamente para qué parámetro está proporcionando un valor utilizando 
argumentos de palabra clave. 
Por ejemplo, greet(name="David", greeting="Salutations") aclara que 
"greet" está destinado al parámetro greeting."""

# Número variable de argumentos (*args y **kwargs)
""" Python permite definir funciones que aceptan un número variable de argumentos. 
Puede utilizar *args para recopilar argumentos posicionales en una tupla 
y **kwargs para recopilar argumentos de palabras clave en un diccionario. """

def flexible_function(*args, **kwargs):
    print("Argumentos posicionales:", args)
    print("Argumentos de palabras clave:", kwargs)

flexible_function(1, 2, 3, name="Alice", age=30)