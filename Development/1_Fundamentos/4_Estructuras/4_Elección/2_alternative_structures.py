""" Python también ofrece estructuras más especializadas como 
    deque (para appends/pops eficientes en ambos extremos), 
    heapq (para colas prioritarias), y collections.COUNT (para contar ocurrencias).
    Pueden resolver problemas específicos de forma más eficiente que 
    las estructuras de datos de propósito general.
    Veamos un ejemplo rápido: """

from collections import deque, Counter

# Deque example
queue = deque()
queue.append("task1")
queue.append("task2")
print(queue.popleft())  # Output: task1

# Counter example
text = "This is a sample text with some repeated words words"
word_counts = Counter(text.split())
print(word_counts)  # Output: Counter({'words': 2, 'This': 1, 'is': 1, ...})