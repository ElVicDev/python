""" Día 81: Programador de tareas
Programe tareas utilizando la biblioteca de programación. """

import schedule
import time

def job():
    print("Haciendo la tarea...")
schedule.every(10).seconds.do(job)
schedule.every().day.at("10:30").do(job)
schedule.every().hour.do(job)
schedule.every().monday.do(job)
schedule.every().wednesday.at("13:15").do(job)
while True:
    schedule.run_pending()
    time.sleep(1)

# Nota: Para detener el programa, use Ctrl+C en la terminal.
# Asegúrese de tener instalada la biblioteca 'schedule' usando: pip install schedule
# Este código ejecutará la función 'job' según el horario definido.
# Puede ajustar los intervalos y horarios según sus necesidades.
# Consulte la documentación de 'schedule' para más opciones: 
# https://schedule.readthedocs.io/en/stable/
# Este es un ejemplo básico y puede expandirse para incluir más funcionalidades 
# según sea necesario.
# Recuerde que este script debe ejecutarse en un entorno que permita la 
# ejecución continua, como una terminal o un servidor.
# También puede agregar manejo de excepciones para mejorar la robustez del programa.
# Este código es útil para automatizar tareas repetitivas en su sistema.
# Puede modificar la función 'job' para realizar cualquier tarea que desee programar.
# ¡Diviértase programando sus tareas!
# ¡Feliz codificación!