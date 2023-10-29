import asyncio
import websockets

async def send_message(message):
    for client in users:
        await client.send(message)

async def get_message(client_socket):
    data = await client_handler.recv()
    print(data)

    return data

users = []

async def client_handler(client_socket):
    print('Подключен новый пользователь')

    users.append(users)

    while True:
        message = await get_message(client_socket)
        await send_message(message)

async def server():
    await websockets.serve(client_handler, 'localhost', 12345)

if __name__ == "__main__":
    event_loop = asyncio.new_event_loop()
    asyncio.set_event_loop(event_loop)
    event_loop.run_until_complete(server())
    event_loop.run_forever()