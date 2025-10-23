""" Día 95: Metaclases
Explora temas avanzados como metaclases. """

# Definición de una metaclase personalizada
class Meta(type):
    def __new__(cls, name, bases, attrs):
        print(f"Creando la clase {name} con metaclase {cls.__name__}")
        return super().__new__(cls, name, bases, attrs)
# Uso de la metaclase en una clase
class MyClass(metaclass=Meta):
    def __init__(self, value):
        self.value = value
    def display(self):
        print(f"Valor: {self.value}")
if __name__ == "__main__":
    # Crear una instancia de MyClass
    obj = MyClass(10)
    obj.display()
""" Resultados esperados:
El programa imprimirá un mensaje indicando que se está creando la clase
'MyClass' con la metaclase 'Meta'. Luego, al crear una instancia de 'MyClass',
se mostrará el valor almacenado en la instancia. """
# Nota: Este código demuestra el uso de metaclases para personalizar la creación
# de clases en Python. Puede ejecutar este código en cualquier entorno Python
# sin necesidad de bibliotecas adicionales.