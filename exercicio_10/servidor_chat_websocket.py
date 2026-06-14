import asyncio
import websockets

connected_clients = set()

async def gestao_cliente(websocket):
    connected_clients.add(websocket)
    try:
        async for message in websocket:
            print(f"Mensagem recebida: {message}")
            for client in connected_clients:
                if client != websocket:
                    await client.send(f"Cliente: {message}")
    except websockets.exceptions.ConnectionClosed:
        print("Cliente desconectado")
    finally:
        connected_clients.remove(websocket)

async def main():
    async with websockets.serve(gestao_cliente, "127.0.0.1", 9000):
        print("Servidor de Chat WebSocket iniciado na porta 9000.")
        await asyncio.Future()  # Mantém o servidor rodando

asyncio.run(main())