""" Día 41: herencia
Implementar la herencia entre clases. """

class Animal:
    """Clase base para todos los animales."""
    def speak(self):
        raise NotImplementedError("El método speak() debe ser implementado por la subclase.")
    def move(self):
        raise NotImplementedError("El método move() debe ser implementado por la subclase.")
class Dog(Animal):
    """Clase que representa un perro."""
    def speak(self):
        return "Woof!"
    def move(self):
        return "The dog runs."
class Cat(Animal):
    """Clase que representa un gato."""
    def speak(self):
        return "Meow!"
    def move(self):
        return "The cat prowls."
class Bird(Animal):
    """Clase que representa un pájaro."""
    def speak(self):
        return "Chirp!"
    def move(self):
        return "The bird flies."
    
# Crear instancias de cada animal
animals = [Dog(), Cat(), Bird()]
for animal in animals:
    print(f"{animal.__class__.__name__} - Speak: {animal.speak()}, Move: {animal.move()}")

# Salida esperada:
# Dog - Speak: Woof!, Move: The dog runs.
# Cat - Speak: Meow!, Move: The cat prowls.
# Bird - Speak: Chirp!, Move: The bird flies.