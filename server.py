import asyncio
import websockets

async def send_message(message,client_socket):
    for client in users:
        await client.send(message)

async def get_message(client_socket):
    data = await client_socket.recv()

    print(data)

    return data
    
users = []

async def client_handler(client_socket):
    try:

        print('Подключен новый пользователь')

        users.append(client_socket)

        while True:
            message = await get_message(client_socket)
            await send_message(message, client_socket)
    
    except Exception as e:
        users.remove(client_socket)

async def server():
    await websockets.serve(client_handler, 'localhost', 1234)

if __name__ == "__main__":
    event_loop = asyncio.new_event_loop()
    asyncio.set_event_loop(event_loop)
    event_loop.run_until_complete(server())
    event_loop.run_forever()