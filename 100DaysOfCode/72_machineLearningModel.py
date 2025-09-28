""" Día 72: Modelo de aprendizaje automático
Entrena un modelo de aprendizaje automático simple (por ejemplo, regresión lineal). """

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt

# Generar datos de ejemplo
np.random.seed(0)
X = 2 * np.random.rand(100, 1)
y = 4 + 3 * X + np.random.randn(100, 1)

# Convertir a DataFrame para facilitar la manipulación
data = pd.DataFrame(np.hstack((X, y)), columns=['Feature', 'Target'])

# Dividir los datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(data[['Feature']], data['Target'], test_size=0.2, random_state=42)

# Crear y entrenar el modelo de regresión lineal
model = LinearRegression()
model.fit(X_train, y_train)

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
plt.plot(X_test, y_pred, color='green', linewidth=2, label='Línea de Regresión')
plt.xlabel('Feature')
plt.ylabel('Target')
plt.title('Regresión Lineal: Datos Reales vs Predicciones')
plt.legend()
plt.show()

# Output:
# Al ejecutar el script, se entrenará un modelo de regresión lineal
# y se mostrarán las métricas de evaluación junto con una visualización
# que compara los datos reales con las predicciones del modelo.

# Comparación con el código del día 71:
# El código del día 71 se centra en la creación de visualizaciones
# de datos interactivas utilizando Plotly y Bokeh,
# mientras que este código del día 72 se enfoca en el entrenamiento
# y evaluación de un modelo de aprendizaje automático utilizando scikit-learn.