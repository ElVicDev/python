""" Día 86: Proyecto Raspberry Pi
Utilice Python para controlar el hardware (por ejemplo, proyectos Raspberry Pi). """

import RPi.GPIO as GPIO
import time
# Configurar el modo de numeración de pines
GPIO.setmode(GPIO.BCM)
# Configurar el pin 18 como salida (LED)
LED_PIN = 18
GPIO.setup(LED_PIN, GPIO.OUT)
# Función para parpadear el LED
def blink_led(pin, duration, blink_times):
    for _ in range(blink_times):
        GPIO.output(pin, GPIO.HIGH)  # Encender LED
        time.sleep(duration)
        GPIO.output(pin, GPIO.LOW)   # Apagar LED
        time.sleep(duration)
# Parpadear el LED 5 veces con una duración de 0.5 segundos
try:
    blink_led(LED_PIN, 0.5, 5)
finally:
    GPIO.cleanup()  # Limpiar la configuración de GPIO

""" Resultados esperados:
El LED conectado al pin 18 parpadeará 5 veces con una duración de 0.5 segundos.
"""
# Nota: Este código debe ejecutarse en una Raspberry Pi con un LED conectado 
# al pin 18.
# Asegúrese de tener los permisos adecuados para acceder a los pines GPIO.
# Además, instale la biblioteca RPi.GPIO si no está ya instalada:
# pip install RPi.GPIO
# El código anterior configura un pin GPIO para controlar un LED, 
# haciendo que parpadee varias veces.
# Asegúrese de ejecutar este código en un entorno adecuado (Raspberry Pi) 
# para ver el efecto físico.