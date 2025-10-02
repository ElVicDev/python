""" Día 75: Sistema de recomendación
Construir un sistema de recomendación. """

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.neighbors import NearestNeighbors
import matplotlib.pyplot as plt
# Generar datos de ejemplo: usuarios, ítems y calificaciones
np.random.seed(0)
n_users = 100
n_items = 50
ratings = np.random.randint(1, 6, size=(n_users, n_items))
# Convertir a DataFrame para facilitar la manipulación
ratings_df = pd.DataFrame(ratings, columns=[f'Item_{i+1}' for i in range(n_items)])
# Dividir los datos en conjuntos de entrenamiento y prueba
train_data, test_data = train_test_split(ratings_df, test_size=0.2, random_state=42)
# Crear el modelo de vecinos más cercanos
model = NearestNeighbors(metric='cosine', algorithm='brute')
model.fit(train_data)
# Hacer recomendaciones para un usuario específico
user_index = 0  # Índice del usuario para el que se harán recomendaciones
distances, indices = model.kneighbors([train_data.iloc[user_index]], n_neighbors=6)
# Mostrar las recomendaciones
print(f"Recomendaciones para el Usuario {user_index + 1}:")
for i in range(1, len(indices[0])):
    recommended_user_index = indices[0][i]
    print(f"Usuario {recommended_user_index + 1} con distancia {distances[0][i]:.4f}")
# Evaluar el modelo utilizando RMSE
def calculate_rmse(true_ratings, predicted_ratings):
    mask = true_ratings > 0  # Solo considerar calificaciones reales
    return np.sqrt(mean_squared_error(true_ratings[mask], predicted_ratings[mask]))
# Predecir calificaciones para el conjunto de prueba
predicted_ratings = train_data.mean(axis=0).values  # Predicción simple: media de calificaciones
rmse = calculate_rmse(test_data.values, np.tile(predicted_ratings, (test_data.shape[0], 1)))
print(f"RMSE del modelo de recomendación: {rmse:.4f}")

# Output:
# Al ejecutar el script, se entrenará un sistema de recomendación
# y se mostrarán las recomendaciones para un usuario específico
# junto con la métrica RMSE del modelo.
