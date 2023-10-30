document.addEventListener('DOMContentLoaded', function(){

    const messageContainer = document.querySelector('.container-messages');
    const messageInput = document.querySelector('.input-block');
    const sendMessageButton = document.querySelector('.button-send');
    
    let websocketClient = new WebSocket('ws://localhost:1234');

    websocketClient.onopen = () => {
        console.log('Клиент подключился!');

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

}, false);