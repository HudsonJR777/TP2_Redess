import socket

# Configuração do servidor
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    server_socket.bind(('127.0.0.1', 5000)) # Liga o servidor ao endereço IP local e à porta 5000

    # Inicia o servidor e aguarda conexões
    server_socket.listen(5)
    print("Servidor esperando conexões...")

    while True:
        client_socket, addr = server_socket.accept()
        print(f"Conexão estabelecida com: {addr}")

        try:
            message = client_socket.recv(1024)
            if not message:
                print(f"Sem mensagem do cliente: {addr}")
            else:
                mensagem_cliente = message.decode()
                print(f"Mensagem do cliente: {mensagem_cliente}")
                client_socket.send(b"Bem-vindo ao servidor! Mensagem recebida")
        
        except socket.error as e:
            print(f"Erro na mensagem do cliente")

        finally:
            client_socket.close()

except socket.error as e:
        print(f"Erro de comunicação na rede: {e}")

finally:
    server_socket.close()