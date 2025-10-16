""" Día 88: Aplicación de chat
Implementar una aplicación de chat usando sockets. """

import socket
import threading

# Configuración del servidor
HOST = '127.0.0.1'  # Dirección IP del servidor
PORT = 65432        # Puerto del servidor
clients = []
nicknames = []
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()
print(f"Servidor iniciado en {HOST}:{PORT}")
def broadcast(message):
    for client in clients:
        client.send(message)
def handle(client):
    while True:
        try:
            message = client.recv(1024)
            broadcast(message)
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[index]
            broadcast(f"{nickname} se ha desconectado.".encode('utf-8'))
            nicknames.remove(nickname)
            break
def receive():
    while True:
        client, address = server.accept()
        print(f"Conectado con {str(address)}")
        client.send('NICK'.encode('utf-8'))
        nickname = client.recv(1024).decode('utf-8')
        nicknames.append(nickname)
        clients.append(client)
        print(f"El apodo del cliente es {nickname}")
        broadcast(f"{nickname} se ha unido al chat!".encode('utf-8'))
        client.send('Conectado al servidor!'.encode('utf-8'))
        thread = threading.Thread(target=handle, args=(client,))
        thread.start()
receive()
""" Resultados esperados:
El servidor de chat se iniciará y podrá aceptar conexiones de clientes.
Los clientes podrán enviar y recibir mensajes en tiempo real.
"""
# Nota: Este es un ejemplo básico de una aplicación de chat.
# Para probarlo, necesitará crear un cliente que se conecte a este servidor.
# Asegúrese de ejecutar este código en un entorno adecuado con acceso a la red.
# Este código no maneja la seguridad ni la autenticación.
# Para una aplicación de chat en producción, considere usar bibliotecas y marcos más robustos.
# Además, este código está diseñado para fines educativos y puede necesitar ajustes
# según sus necesidades específicas.
# Asegúrese de tener Python instalado en su sistema para ejecutar este código.
# Puede ejecutar este script en la terminal o en un entorno de desarrollo integrado (IDE).
# El código anterior crea un servidor de chat que escucha conexiones entrantes
# y permite a los clientes enviar y recibir mensajes en tiempo real.
