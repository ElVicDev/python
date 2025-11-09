def linear_search(data, target):
    """
    Realiza una búsqueda lineal en una lista para encontrar el índice del elemento objetivo.

    Parámetros:
    data (list): La lista en la que se realizará la búsqueda.
    target: El elemento que se desea buscar en la lista.

    Retorna:
    int: El índice del elemento objetivo si se encuentra; de lo contrario, -1.
    """
    # Validate if the input data is a list
    if not isinstance(data, list):
        return "Invalid input: data must be a list."
    
    # Handle the case of an empty list
    if not data:
        return -1
    
    # Iterate through the list using its index
    for i in range(len(data)):
        if data[i] == target:
            return i  # Return the index if the target is found
        
    # If the loop completes without finding the target, return -1
    return -1

list_example = ["Hello", "World", "Good", "Day", "To", "You"]

search_1 = linear_search(list_example, "Day") # Found in index 3
print("result of searching for 'Day':", search_1)

search_2 = linear_search(list_example, "Python") # Not found
print("result of searching for 'Python':", search_2)