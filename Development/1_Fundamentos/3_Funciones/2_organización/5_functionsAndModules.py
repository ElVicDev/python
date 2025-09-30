# EXERCISE 1:
""" El código inicial tiene una llamada a una función, happy_birthday, 
    que usted escribirá.
    Escriba la definición de la función, happy_birthday, que no toma 
    parámetros (1 línea de código). 
    Evite las sugerencias de tipo para los parámetros.
    La función debe imprimir Happy Birthday! para el usuario 
    (1 línea de código). La función no debe devolver ningún valor. 
    Asegúrese de que las mayúsculas coinciden exactamente 
    (H mayúscula y B mayúscula) y de que incluye el signo de exclamación.
    Ejecute el programa. El programa mostrará siempre el mismo mensaje. """
def happy_birthday():
    print("Happy Birthday!")

# Code to call the function
happy_birthday()


# EXERCISE 2:
""" El código inicial tiene una llamada a una función, happy_birthday, 
    que usted escribirá.
    Escriba la definición de la función, happy_birthday, que toma dos 
    parámetros, el primero llamado age y el segundo llamado name 
    (1 línea de código). Evite las sugerencias de tipo para los parámetros.
    La función debe imprimir Happy Birthday <name> and congratulations 
    on turning <age> years old! para el usuario (1 línea de código). 
    Por ejemplo, si pasa los valores 22 para la edad y Nora para el nombre, 
    el programa debe mostrar Happy Birthday Nora and congratulations on 
    turning 22 years old!. La función no debe devolver ningún valor. 
    Asegúrese de que el espaciado es coherente con los requisitos 
    (por ejemplo, "Feliz cumpleaños Nora" tiene dos espacios entre 
    "Cumpleaños" y "Nora" cuando debería tener uno).
    Ejecute el programa. ASÍ COMO ESTÁ ESCRITO, siempre mostrará el 
    mismo mensaje, pero podría modificarse para aceptar entradas en 
    lugar de utilizar siempre los mismos valores. """
def happy_birthday(age, name):
    print("Happy Birthday",name,"and congratulations on turning",age,"years old!")

# Code to call the function
happy_birthday(22, "Nora")


# EXERCISE 3:
""" Comience escribiendo la definición de función para una función 
    get_lucky_number. Recuerde, esta función no debe requerir ningún 
    parámetro de entrada (una línea de código). 
    Evite las sugerencias de tipo para el valor de retorno.
    A continuación, la función debe devolver el valor de lucky_num 
    (una línea de código). El valor ya ha sido cargado; su tarea es 
    devolver el valor al programa principal.
    Ejecute el programa. Se generará un número aleatorio en el rango 
    (1 a 100, como se define en la función). 
    Esto permite escribir la lógica una vez y reutilizarla muchas veces 
    en el programa. """
import random

def get_lucky_number():
  lucky_num = random.randint(1,100)
  return lucky_num

# Get a lucky number between 1 and 100
lucky_number = get_lucky_number()

print("Your lucky number is:", lucky_number)


# EXERCISE 4:
""" Empiece escribiendo la definición de la función calc_sale_price. 
    Esta función aceptará dos parámetros de entrada (una línea de código). 
    El primero, amount, es un número que representa el importe de la compra. 
    El segundo, member, es una variable booleana que representa si el usuario 
    es socio (True) o no (False). 
    Evite las sugerencias de tipo para los parámetros y el tipo de retorno.
    Redondee amount a dos decimales utilizando la función integrada round. 
    Guarde el resultado en la variable amount.
    La función debe devolver el valor de amount. 
    Ejecute el código. Se mostrarán los importes descontados. """
def calc_sale_price(amount, member):
    if member:
        # Members receive a 15% discount (0.15)
        amount = amount - (amount * 0.15)
    else:
        # Non-members get a 5% discount (0.05)
        amount = amount - (amount * 0.05)
    amount = round(amount,2)
    
    # Insert code here
    return amount

# Example price (already provided)
full_price = 150.50

# Call function for members
member_price = calc_sale_price(full_price, True)
print("Member price:",member_price)

# Call function for non-members
non_member_price = calc_sale_price(full_price, False)
print("Non-member price:",non_member_price)


# EXERCISE 5:
""" 1. Ejecute el código siguiente y observe el error. 
      La primera llamada a una función, display_color_works(), se ejecutará 
      correctamente. La segunda, display_color_failure(), resultará en un 
      NameError.
    2. Hay varias maneras de corregir esto.
      a. Una forma es comentar la línea que llama a display_color_failure. 
          Esto no soluciona el problema, pero evita el error.
      b. La forma preferida es establecer shirt_color fuera de la función 
          display_color_works, en el programa principal, y pasar el valor 
          a ambas funciones.
      c. Una tercera forma es atrapar el error utilizando un bloque try/catch.
      d. Una cuarta forma es declarar la variable como una variable global, 
        pero como se discutió en una lectura anterior, esto se considera 
        una mala práctica.
    3. Comente la llamada a la función display_color_failure y vuelva a 
      ejecutar el programa. Comprueba que el error desaparece.    """
# def display_color_failure():
  # Try to access 'color' directly (this will cause an error)
  # print("Your shirt color is:", shirt_color)

def display_color_works():
  shirt_color = "Pink"
  print("First shirt color is:", shirt_color)

# The shirt_color variable is in scope in this function
display_color_works()

# The shirt_color variable is not in scope in this function
#display_color_failure()


# EXERCISE 6:
""" Usted ha creado un archivo llamado menus.py almacenado en la misma carpeta 
    que su programa actual. Este módulo contiene una función, display_menu, 
    que ha sido escrita. No toma argumentos y devuelve un valor numérico.
    Importa el módulo menus para que su contenido esté disponible en tu programa.
    Introduzca el código para llamar al módulo display_menu en el módulo de menús. 
    El resultado se guardará en la variable user_choice.
    Este código requiere un archivo menus.py. 
    Funcionará en la plataforma Coursera, pero no funcionaría en un editor 
    de código separado en su sistema.
    Diseñar de esta manera permite a otro programador modificar el módulo 
    de menús independientemente de su código, y su programa se beneficiará 
    de la última actualización. """
# import the menus module (menus.py needs to exist)
import menus

# Call the display_menu function in the menus module
user_choice = menus.display_menu()

print(user_choice)