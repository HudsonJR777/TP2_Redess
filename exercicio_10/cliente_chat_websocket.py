# Hudson Junior, Janaina Alves, Luiz Otávio, Tiago Secundo 
import asyncio
import websockets

# Função para receber mensagens do servidor
async def receber_mensagens(websocket):
    try:
        async for message in websocket:
            print(f"\n{message}")
    except websockets.exceptions.ConnectionClosed:
        print("Conexão fechada pelo servidor")

# Função para enviar mensagens ao servidor
async def enviar_mensagens(websocket, nome):
    loop = asyncio.get_event_loop() # Permite usar input sem bloquear a execução do loop de eventos, evitando travar a recepção de mensagens enquanto o usuário digita.
    while True:
        mensagem = await loop.run_in_executor(None, input, f"[{nome}]: ") # Permite entrada de mensagens sem bloquear a recepção(usando input trava a execução)
        if mensagem.lower().strip() == "sair":
            await websocket.close()
            break
        else:
            await websocket.send(mensagem)

# Função principal para conectar ao servidor e iniciar as tarefas de envio e recepção de mensagens
async def main():
    uri = "ws://127.0.0.1:9000" # Endereço para conectar ao servidor WebSocket
    try:
        async with websockets.connect(uri) as websocket:
            print("Conectado ao servidor de chat WebSocket!")
            nome = input("Digite seu nome: ")
            await asyncio.gather(receber_mensagens(websocket), enviar_mensagens(websocket, nome))
    except ConnectionRefusedError:
        print("Não foi possível conectar ao servidor. Verifique se o servidor está em execução.")
    except websockets.exceptions.ConnectionClosed:
        print("Conexão fechada pelo servidor.")
    
asyncio.run(main())