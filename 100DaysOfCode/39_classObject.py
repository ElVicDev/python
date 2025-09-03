""" Día 39: Objeto de clase
Cree una clase para un automóvil simple con métodos como Start and Stop. """

class Car:
    """Clase que representa un automóvil simple."""
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.is_running = False

    def start(self):
        """Método para arrancar el automóvil."""
        if not self.is_running:
            self.is_running = True
            return f"{self.year} {self.make} {self.model} ha arrancado."
        else:
            return f"{self.year} {self.make} {self.model} ya está en marcha."

    def stop(self):
        """Método para detener el automóvil."""
        if self.is_running:
            self.is_running = False
            return f"{self.year} {self.make} {self.model} se ha detenido."
        else:
            return f"{self.year} {self.make} {self.model} ya está detenido."

# Crear una instancia de la clase Car
my_car = Car("Toyota", "Corolla", 2025)
print(my_car.start())  # Salida: 2020 Toyota Corolla ha arrancado.
print(my_car.start())  # Salida: 2020 Toyota Corolla ya está en marcha
print(my_car.stop())   # Salida: 2020 Toyota Corolla se ha detenido.
print(my_car.stop())   # Salida: 2020 Toyota Corolla ya está detenido.
