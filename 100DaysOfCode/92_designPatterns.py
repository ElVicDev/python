""" Día 92: Patrones de diseño
Estudiar e implementar patrones de diseño en Python. """

class Singleton:
    """Patrón Singleton: Asegura que una clase tenga solo una instancia."""
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance

class Factory:
    """Patrón Factory: Crea objetos sin exponer la lógica de creación al cliente."""
    @staticmethod
    def create_animal(animal_type):
        if animal_type == 'dog':
            return Dog()
        elif animal_type == 'cat':
            return Cat()
        else:
            raise ValueError("Unknown animal type")

class Dog:
    def speak(self):
        return "Woof!"

class Cat:
    def speak(self):
        return "Meow!"

if __name__ == "__main__":
    # Probar el patrón Singleton
    singleton1 = Singleton()
    singleton2 = Singleton()
    print("Singleton Test:")
    print(f"singleton1 is singleton2: {singleton1 is singleton2}")  # Debería ser True

    # Probar el patrón Factory
    print("\nFactory Test:")
    dog = Factory.create_animal('dog')
    cat = Factory.create_animal('cat')
    print(f"Dog says: {dog.speak()}")
    print(f"Cat says: {cat.speak()}")
""" Resultados esperados:
El programa imprimirá que singleton1 y singleton2 son la misma instancia (True) 
y mostrará los sonidos del perro y el gato. """
# Nota: Este código demuestra dos patrones de diseño comunes: Singleton y Factory.
# El patrón Singleton asegura que una clase tenga solo una instancia,
# mientras que el patrón Factory proporciona una interfaz para crear objetos
# sin exponer la lógica de creación al cliente.
# Puede ejecutar este código en cualquier entorno Python sin necesidad de 
# bibliotecas adicionales.
# Asegúrese de entender cómo funcionan estos patrones y considere aplicarlos 
# en sus propios proyectos.