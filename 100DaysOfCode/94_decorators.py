""" Día 94: Decoradores y descriptores
Experimente con decoradores y descriptores. """

def my_decorator(func):
    """Un decorador simple que imprime mensajes antes y después de la ejecución de una función."""
    def wrapper(*args, **kwargs):
        print(f"Ejecutando la función '{func.__name__}'...")
        result = func(*args, **kwargs)
        print(f"Función '{func.__name__}' ejecutada.")
        return result
    return wrapper
@my_decorator
def say_hello(name):
    """Función que saluda a una persona por su nombre."""
    print(f"Hola, {name}!")
class Descriptor:
    """Un descriptor simple que gestiona el acceso a un atributo."""
    def __init__(self, name):
        self.name = name
    def __get__(self, instance, owner):
        print(f"Obteniendo el valor de '{self.name}'")
        return instance.__dict__.get(self.name, None)
    def __set__(self, instance, value):
        print(f"Estableciendo el valor de '{self.name}' a '{value}'")
        instance.__dict__[self.name] = value
class Person:
    """Clase que utiliza un descriptor para gestionar el atributo 'age'."""
    age = Descriptor('age')
    def __init__(self, name, age):
        self.name = name
        self.age = age
if __name__ == "__main__":
    # Usar el decorador
    say_hello("Carlos")
    # Usar el descriptor
    p = Person("Ana", 30)
    print(f"{p.name} tiene {p.age} años.")
    p.age = 31
    print(f"{p.name} ahora tiene {p.age} años.")

""" Resultados esperados:
El programa imprimirá mensajes indicando cuándo se está ejecutando la función
'say_hello', junto con el saludo. Luego, al crear una instancia de la clase
'Person', se mostrarán mensajes del descriptor al obtener y establecer el
atributo 'age'. """
# Nota: Este código demuestra el uso de decoradores para modificar el comportamiento
# de funciones y descriptores para gestionar el acceso a atributos en clases.
# Puede ejecutar este código en cualquier entorno Python sin necesidad de
# bibliotecas adicionales.