import asyncio
import websockets

async def receber_mensagens(websocket):
    try:
        async for message in websocket:
            print(f"/n{message}")
    except websockets.exceptions.ConnectionClosed:
        print("Conexão fechada pelo servidor")

async def enviar_mensagens(websocket, nome):
    loop = asyncio.get_event_loop()
    while True:
        mensagem = await loop.run_in_executor(None, input, f"[{nome}]: ")
        if mensagem.lower().strip() == "sair":
            await websocket.close()
            break
        else:
            await websocket.send(mensagem)

async def main():
    uri = "ws://127.0.0.1:9000"
    try:
        async with websockets.connect(uri) as websocket:
            print("Conectado ao servidor de chat WebSocket!")
            nome = input("Digite seu nome: ")
            await asyncio.gather(receber_mensagens(websocket), enviar_mensagens(websocket, nome))
    except ConnectionRefusedError:
        print("Não foi possível conectar ao servidor. Verifique se o servidor está em execução.")
    
asyncio.run(main())