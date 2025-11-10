def binary_search(data, target):
    """
    Realiza una búsqueda binaria en una lista ordenada para encontrar el índice del elemento objetivo.

    Parámetros:
    data (list): La lista ordenada en la que se realizará la búsqueda.
    target: El elemento que se desea buscar en la lista.

    Retorna:
    int: El índice del elemento objetivo si se encuentra; de lo contrario, -1.
    """

    low = 0 # Initialize the begginning of the search interval
    high = len(data) - 1 # Initialize the end of the search interval

    # Continue searching as long as the lower bound is less than or equal to the upper bound
    while low <= high:
        # Calculate the middle index of the current search interval
        mid = (low + high) // 2 # Use integer division to find the middle index

        # Check if the element at the middle index is the target
        if data[mid] == target:
            return mid  # If found, return the index
        # If the element at the middle index is less than the target,
        # discard the left half and search in the upper half
        elif data[mid] < target:
            low = mid + 1
        # If the element at the middle index is greater than the target,
        # discard the right half and search in the lower half
        else:   # data[mid] > target
            high = mid - 1

    # If the loop finishes, it means the target is not in the list
    return -1

# Note: For binary search to work correctly, the input list must be sorted.
list_example = [0, 1, 2, 3, 4, 5, 9, 87, 165]

search_value_1 = 50
result_1 = binary_search(list_example, search_value_1) # Not found
print(result_1) # 50 is not found in the list (returns -1)

search_value_2 = 87
result_2 = binary_search(list_example, search_value_2)
print(result_2) # 87 is found at index 7
