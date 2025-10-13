""" Día 83: herramienta de línea de comandos
Cree una herramienta de línea de comandos con argparse. """

import argparse

def main():
    parser = argparse.ArgumentParser(description="Herramienta de línea de comandos simple")
    parser.add_argument("nombre", type=str, help="Tu nombre")
    parser.add_argument("--edad", type=int, help="Tu edad", default=18)
    parser.add_argument("--ciudad", type=str, help="Tu ciudad", default="Desconocida")

    args = parser.parse_args()

    print(f"Hola, {args.nombre}!")
    print(f"Tienes {args.edad} años.")
    print(f"Vives en {args.ciudad}.")

if __name__ == "__main__":
    main()
# Ejemplo de uso:
# python 83_commandLine.py Juan --edad 25 --ciudad Madrid
# Salida esperada:
# Hola, Juan!
# Tienes 25 años.
# Vives en Madrid.
# python 83_commandLine.py Ana
# Salida esperada:
# Hola, Ana!
# Tienes 18 años.
# Vives en Desconocida.
# El objetivo de esta actividad es introducir clases, métodos y funciones, 
# así como algunas de las consideraciones a tener en cuenta a la hora de
# decidir qué incluir en las clases.