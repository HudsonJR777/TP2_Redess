import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:    
    client_socket.connect(('127.0.0.1', 8000))
    
    message_server = client_socket.recv(1024)
    print(message_server.decode())

except socket.error as e:
    print(f"Erro de comunicação na rede: {e}")

finally:
    client_socket.close()