import asyncio
import websockets

async def send_message(message,client_socket):
    for client in users:
        await client.send(f'{users[client_socket]} : {message}')

async def get_message(client_socket):
    data = await client_socket.recv()

    return data
    
users = {}

async def client_handler(client_socket):
    try:
        date = await client_socket.recv()

        users[client_socket] = date

        print('Подключен новый пользователь')

        for client in users:
            await client_socket.send(f'{users[client]} вошел в чат !')

        while True:
            message = await get_message(client_socket)
            await send_message(message, client_socket)
    
    except Exception as e:
        del users[client_socket]

async def server():
    await websockets.serve(client_handler, 'localhost', 1234)

if __name__ == "__main__":
    event_loop = asyncio.new_event_loop()
    asyncio.set_event_loop(event_loop)
    event_loop.run_until_complete(server())
    event_loop.run_forever()