""" Día 76: Chatbot
Cree un chatbot usando bibliotecas NLP. """

import nltk
from nltk.chat.util import Chat, reflections
# Descargar recursos necesarios de NLTK (solo la primera vez)
nltk.download('punkt')
# Definir pares de patrones y respuestas
pairs = [
    (r'Hola|Hola|Hey', ['Hola, ¿cómo puedo ayudarte?', '¡Hola! ¿En qué puedo asistirte?']),
    (r'¿Cómo estás\??', ['Estoy bien, gracias. ¿Y tú?', '¡Muy bien! ¿Y tú?']),
    (r'¿Cuál es tu nombre\??', ['Soy un chatbot creado para ayudarte.', 'Puedes llamarme Chatbot.']),
    (r'¿Qué puedes hacer\??', ['Puedo responder a tus preguntas y ayudarte con información.', 'Estoy aquí para asistirte en lo que necesites.']),
    (r'Adiós|Chao|Hasta luego', ['¡Adiós! Que tengas un buen día.', '¡Hasta luego!']),
    (r'(.*)', ['Lo siento, no entiendo eso.', '¿Puedes reformular tu pregunta?'])
]
# Crear el chatbot
chatbot = Chat(pairs, reflections)
# Iniciar la conversación
print("Hola, soy tu chatbot. Escribe 'salir' para terminar la conversación.")
while True:
    user_input = input("Tú: ")
    if user_input.lower() in ['salir', 'adiós', 'chao']:
        print("Chatbot: ¡Adiós! Que tengas un buen día.")
        break
    response = chatbot.respond(user_input)
    print(f"Chatbot: {response}")
# Output:
# Al ejecutar el script, se iniciará una conversación con el chatbot.