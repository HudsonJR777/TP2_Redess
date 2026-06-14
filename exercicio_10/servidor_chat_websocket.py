import asyncio
import websockets

connected_clients = set() # Conjunto para armazenar os clientes conectados

# Função para gerenciar a comunicação com cada cliente
async def gestao_cliente(websocket):
    connected_clients.add(websocket) # Adiciona o cliente à lista de clientes conectados
    try:
        # Permite receber mensagens do cliente e encaminhá-las para os outros clientes conectados
        async for message in websocket:
            print(f"Mensagem recebida: {message}")
            # Encaminha a mensagem para todos os outros clientes conectados
            for client in connected_clients:
                if client != websocket:
                    await client.send(f"Cliente: {message}")
    except websockets.exceptions.ConnectionClosed:
        print("Cliente desconectado")
    finally:
        connected_clients.remove(websocket)

# Função principal para iniciar o servidor WebSocket
async def main():
    async with websockets.serve(gestao_cliente, "127.0.0.1", 9000):
        print("Servidor de Chat WebSocket iniciado na porta 9000.")
        await asyncio.Future()  # Mantém o servidor rodando

asyncio.run(main())