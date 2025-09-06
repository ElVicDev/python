""" Día 46: decoradores de clase
Use decoradores de clase en Python. """

def decorator(cls):
    """Un decorador simple que añade un método a la clase."""
    def new_method(self):
        return "Este es un nuevo método añadido por el decorador."
    
    cls.new_method = new_method
    return cls

@decorator
class MyClass:
    def __init__(self, value):
        self.value = value

    def display(self):
        return f"Value: {self.value}"
    
# Crear una instancia de MyClass
obj = MyClass(10)
print(obj.display())          # Muestra el valor
print(obj.new_method())      # Llama al nuevo método añadido por el decorador

# Salida esperada:
# Value: 10
# Este es un nuevo método añadido por el decorador.