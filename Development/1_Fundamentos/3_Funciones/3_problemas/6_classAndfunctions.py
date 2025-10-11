# El objetivo de esta actividad es introducir clases, métodos y funciones, 
# así como algunas de las consideraciones a tener en cuenta a la hora de 
# decidir qué incluir en las clases.

""" Está trabajando con un grupo de estudiantes de ciencias medioambientales 
    que controlan la temperatura (en grados Fahrenheit) en distintos puntos 
    de un bosque.
    Han colocado varios sensores en distintos puntos del bosque para recoger 
    datos sobre la temperatura. 
    Los datos de estos sensores se registran automáticamente y se almacenan 
    en una base de datos. 
    Necesita recuperar estos datos de los sensores, analizarlos en busca 
    de tendencias o anomalías, y potencialmente identificar microclimas 
    dentro del bosque.  """

class TemperatureData:
    # Constructor to create object
    def __init__(self, name, readings):
        self.name = name
        self.readings = readings

    # Calculate average temperatures
    def calculate_average_temp(self):
        return sum(self.readings) / len(self.readings)

    # Find highest temperature
    def find_high_temp(self):
        return max(self.readings)

    # Find lowest temperature
    def find_low_temp(self):
        return min(self.readings)
    
    # Find temperature range (max-min)
    def calc_range(self):
        return max(self.readings) - min(self.readings)
    
""" Programa principal """
# Create a name for a sensor
sensor_name = "East Forest Road Sensor"

sensor = TemperatureData(sensor_name, [75, 71, 68, 64, 88])

average_temp = sensor.calculate_average_temp()
print(f"Average temperature for sensor {sensor_name}: {average_temp} degrees Fahrenheit")

highest = sensor.find_high_temp()
lowest = sensor.find_low_temp()
print(f"Temperature extremes for sensor {sensor_name}: Highest {highest}, Lowest {lowest}") 
# Code above this point is unchanged, except for removing the function

# New call to method in TemperatureData
range = sensor.calc_range()
print(f"Temperature range for sensor {sensor_name}: {range} degrees Fahrenheit")

""" Resultados esperados: """
# Average temperature for sensor East Forest Road Sensor: 73.2 degrees Fahrenheit
# Temperature extremes for sensor East Forest Road Sensor: Highest 88, Lowest 64
# Temperature range for sensor East Forest Road Sensor: 24 degrees Fahrenheit