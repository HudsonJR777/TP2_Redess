import socket

# Configuração do cliente
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:    
    client_socket.connect(('127.0.0.1', 5000))

    mensagem = input("Digite a mensagem ao servidor: ")

    if mensagem.strip() == "":
        print("Não é permitido enviar mensagens vazias")
    else:
        client_socket.send(mensagem.encode())
        message_server = client_socket.recv(1024)
        print(f"Mensagem do servidor: {message_server.decode()}")

except socket.error as e:
    print(f"Erro de comunicação na rede: {e}")

finally:
    client_socket.close()