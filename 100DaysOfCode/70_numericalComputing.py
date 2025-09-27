""" Día 70: Computación numérica
Use Numpy para la computación numérica. """

import numpy as np

# Crear un array NumPy
data = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("Array NumPy:")
print(data)

# Operaciones básicas
mean = np.mean(data)
median = np.median(data)
std_dev = np.std(data)
print(f"\nMedia: {mean}")
print(f"Mediana: {median}")
print(f"Desviación Estándar: {std_dev}")

# Operaciones avanzadas
transposed = np.transpose(data)
inverted = np.linalg.inv(data)
eigenvalues, eigenvectors = np.linalg.eig(data)
print("\nTranspuesta del Array:")
print(transposed)
print("\nInversa del Array:")
print(inverted)
print("\nValores Propios:")
print(eigenvalues)
print("\nVectores Propios:")
print(eigenvectors)
# Operaciones con arrays
array_sum = np.sum(data, axis=0)
array_product = np.prod(data, axis=1)
print(f"\nSuma por columnas: {array_sum}")
print(f"Producto por filas: {array_product}")
# Generar datos aleatorios
random_data = np.random.rand(3, 3)
print("\nDatos Aleatorios:")
print(random_data)
# Guardar y cargar arrays
np.save('array_data.npy', data)
loaded_data = np.load('array_data.npy')
print("\nArray cargado desde 'array_data.npy':")
print(loaded_data)

# Output:
# Al ejecutar el script, se crearán y mostrarán varios arrays NumPy,
# se realizarán operaciones estadísticas y algebraicas,
# y se guardará y cargará un array desde un archivo .npy.

# Comparación con el código del día 69:
# El código del día 69 realiza un análisis estadístico en un conjunto de datos
# utilizando pandas y scipy, mientras que este código del día 70 se centra en
# la computación numérica utilizando NumPy.