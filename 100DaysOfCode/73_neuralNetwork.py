""" Día 73: Red neuronal
Implemente una red neuronal usando TensorFlow o Pytorch. """

import numpy as np
import pandas as pd
import tensorflow as tf
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt
from tensorflow.keras import layers, models
# Generar datos de ejemplo
np.random.seed(0)
X = 2 * np.random.rand(1000, 1)
y = 4 + 3 * X + np.random.randn(1000, 1)
# Convertir a DataFrame para facilitar la manipulación
data = pd.DataFrame(np.hstack((X, y)), columns=['Feature', 'Target'])
# Dividir los datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(data[['Feature']], data['Target'], test_size=0.2, random_state=42)
# Escalar los datos
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)
# Crear el modelo de red neuronal
model = models.Sequential()
model.add(layers.Dense(64, activation='relu', input_shape=(X_train.shape[1],)))
model.add(layers.Dense(64, activation='relu'))
model.add(layers.Dense(1))
# Compilar el modelo
model.compile(optimizer='adam', loss='mse')
# Entrenar el modelo
model.fit(X_train, y_train, epochs=100, batch_size=32, validation_split=0.2, verbose=0)
# Hacer predicciones
y_pred = model.predict(X_test)
# Evaluar el modelo
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
print(f"Mean Squared Error: {mse}")
print(f"R^2 Score: {r2}")
# Visualizar los resultados
plt.scatter(X_test, y_test, color='blue', label='Datos Reales')
plt.scatter(X_test, y_pred, color='red', label='Predicciones')
plt.xlabel('Feature')
plt.ylabel('Target')
plt.title('Red Neuronal: Datos Reales vs Predicciones')
plt.legend()
plt.show()
# Output:
# Al ejecutar el script, se entrenará una red neuronal
# y se mostrarán las métricas de evaluación junto con una visualización
# que compara los datos reales con las predicciones del modelo.

# Comparación con el código del día 72:
# El código del día 72 se centra en el entrenamiento de un modelo de regresión line
# y la evaluación de su rendimiento utilizando métricas como el error cuadrático medio y el R^2.
# En contraste, este código del día 73 implementa una red neuronal utilizando TensorFlow,
# lo que permite capturar relaciones más complejas en los datos.