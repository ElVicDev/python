# Algoritmos de ordenación: una comparación entre un método simple y quicksort
""" Imagina que intentas ordenar una baraja de cartas en orden numérico. 
    Un método sería encontrar la carta más baja, apartarla, luego encontrar 
    la siguiente carta más baja, y así sucesivamente. 
    Este método es sencillo de entender, pero tardaría una eternidad 
    si se tratara de una baraja enorme. 
    En Python, podrías escribir un algoritmo básico de ordenación como éste: """

def simple_sort(cards):
    sorted_cards = []
    while cards:
        lowest_card = min(cards)  
        sorted_cards.append(lowest_card)
        cards.remove(lowest_card)
    return sorted_cards

""" Un algoritmo diferente, como quicksort, está diseñado específicamente para 
    ordenar y sería mucho más rápido, especialmente para barajas grandes. 
    Podría ser algo parecido a esto:   """

def quicksort(cards):
    if len(cards) < 2:
        return cards  # Caso base: Ya ordenado si hay 0 o 1 elemento
    else:
        pivot = cards[0]  # Elija la primera carta como pivote
        less = [i for i in cards[1:] if i <= pivot]
        greater = [i for i in cards[1:] if i > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)
    
# Puntos clave sobre quicksort:
""" Quicksort descompone el problema eligiendo un elemento "pivote" y dividiendo 
    el resto de las cartas en menores o iguales que el pivote y mayores que el 
    pivote.

    A continuación, ordena recursivamente las sublistas "menores que" 
    y "mayores que", combinándolas finalmente con el pivote para obtener un 
    resultado totalmente ordenado.

    En el caso medio, la ordenación rápida es mucho más rápida que los algoritmos 
    de ordenación más sencillos, como el mostrado anteriormente. 
    Esto es especialmente cierto para grandes conjuntos de datos, donde su 
    ventaja de rendimiento es aún más pronunciada. """