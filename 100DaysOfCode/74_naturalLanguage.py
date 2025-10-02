""" Día 74: Procesamiento del lenguaje natural
Realice tareas de procesamiento del lenguaje natural (por ejemplo, análisis de sentimientos). """

import numpy as np
import pandas as pd
import nltk
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns
# Descargar recursos de NLTK
nltk.download('punkt')
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
# Datos de ejemplo: reseñas de películas y sus etiquetas (positivo/negativo)
data = {
    'review': [
        "I loved the movie, it was fantastic!",
        "What a terrible film, I hated it.",
        "An amazing experience, would watch again.",
        "Not my cup of tea, quite boring.",
        "A masterpiece of cinema, truly inspiring.",
        "Awful plot and poor acting.",
        "Brilliant storyline and great characters.",
        "I fell asleep, it was so dull.",
        "A thrilling ride from start to finish!",
        "Waste of time, do not recommend."
    ],
    'sentiment': [
        'positive', 'negative', 'positive', 'negative', 'positive',
        'negative', 'positive', 'negative', 'positive', 'negative'
    ]
}
df = pd.DataFrame(data)
# Preprocesamiento de texto
stop_words = set(stopwords.words('english'))
def preprocess_text(text):
    tokens = word_tokenize(text.lower())
    filtered_tokens = [word for word in tokens if word.isalnum() and word not in stop_words]
    return ' '.join(filtered_tokens)
df['cleaned_review'] = df['review'].apply(preprocess_text)
# Dividir los datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(df['cleaned_review'], df['sentiment'], test_size=0.2, random_state=42)
# Vectorización de texto
vectorizer = CountVectorizer()
X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)
# Entrenar un modelo de Naive Bayes
model = MultinomialNB()
model.fit(X_train_vec, y_train)
# Hacer predicciones
y_pred = model.predict(X_test_vec)
# Evaluar el modelo
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy}")
print("Classification Report:")
print(classification_report(y_test, y_pred))
# Matriz de confusión
cm = confusion_matrix(y_test, y_pred)
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=['negative', 'positive'], yticklabels=['negative', 'positive'])
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.title('Confusion Matrix')
plt.show()
# Output:
# Al ejecutar el script, se entrenará un modelo de análisis de sentimientos
# y se mostrarán las métricas de evaluación junto con una matriz de confusión visual.

# Comparación con el código del día 73:
# El código del día 73 se centra en la implementación de una red neuronal para un problema
# de regresión utilizando TensorFlow. En contraste, este código del día 74 se enfoca en
# el procesamiento del lenguaje natural y la clasificación de texto utilizando un modelo
# de Naive Bayes. Ambos códigos demuestran técnicas de aprendizaje automático, pero en
# diferentes dominios y con diferentes enfoques de modelado.