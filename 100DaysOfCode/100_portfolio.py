""" Día 100: Portafolio
Cree una cartera de proyectos de Python para mostrar sus habilidades. """

def create_portfolio():
    """
    Esta función es un marcador de posición para representar la creación
    de un portafolio de proyectos. En un escenario real, podrías compilar
    tus proyectos en un sitio web o repositorio dedicado.
    """
    print("Creando portafolio de proyectos de Python...")
    # Aquí podrías agregar código para generar un sitio web o un archivo README
    # que muestre tus proyectos, pero eso está fuera del alcance de este ejemplo simple.
    print("¡Portafolio creado!")
if __name__ == "__main__":
    create_portfolio()
""" Tuplas y conjuntos en acción """
# Tuples
coordinates = (37.7749, -122.4194)  # Latitude, longitude of San Francisco
birth_date = (1990, 12, 25)       # Year, month, day
# Sets
unique_colors = {"red", "green", "blue"}
numbers = [1, 2, 2, 3, 4, 4, 5]
unique_numbers = set(numbers)    # Removes duplicates
""" Las tuplas se utilizan a menudo cuando necesitas asegurarte de que los 
    datos permanecen constantes a lo largo de tu programa. 
    Por ejemplo, puedes utilizar una tupla para almacenar coordenadas 
    (latitud y longitud), ya que no querrás que cambien accidentalmente. 
    Los conjuntos son excelentes para tareas como eliminar duplicados de una 
    lista o comprobar si un elemento existe dentro de una colección. """