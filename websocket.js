document.addEventListener('DOMContentLoaded', function(){

    const messageContainer = document.querySelector('.container-messages');
    const messageInput = document.querySelector('.input-block');
    const sendMessageButton = document.querySelector('.button-send');
    
    let websocketClient;

    sendMessageButton.onclick = () => {
        const name = prompt("Enter your name:");
        if(name){
            websocketClient = new WebSocket('ws://localhost:1234');
            websocketClient.onopen = () => {
                console.log('Клиент подключился!');
                websocketClient.send(name);
                sendMessageButton.onclick = () => {
                    websocketClient.send(messageInput.value);
                    messageInput.value = "";
                };
            };

            websocketClient.onmessage = (message) => {
                const newMessage = document.createElement('div');
                newMessage.innerHTML = message.data;
                messageContainer.appendChild(newMessage);
            }
        }
    };

}, false);