""" Día 44: Definición de clase
Cree una clase para un libro con atributos como el título y el autor. """

class Book:
    """Clase que representa un libro con título y autor."""
    def __init__(self, title, author):
        self.title = title      # Atributo público
        self.author = author    # Atributo público

    def get_info(self):
        """Devuelve la información del libro."""
        return f"'{self.title}' by {self.author}"
    
# Crear una instancia de Book
book = Book("1984", "George Orwell")
print(book.get_info())  # Información del libro

# Salida esperada:
# '1984' by George Orwell