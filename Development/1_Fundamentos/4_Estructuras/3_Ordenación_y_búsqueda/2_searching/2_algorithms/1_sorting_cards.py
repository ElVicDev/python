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