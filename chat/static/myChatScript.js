const userName = JSON.parse(document.getElementById('user-name').textContent);
const roomName = JSON.parse(document.getElementById('room-name').textContent);

const message_form = document.querySelector('#chat-log');

const socket = new WebSocket(
  'ws://'
  + window.location.host
  + '/ws/chat/'
  + roomName
  + '/'
);

socket.onmessage = function(e) {
  const data = JSON.parse(e.data);
  appendMessage("Chatbot", "left", data.response);
};


document.querySelector('#chat-message-submit').onclick = function() {
    const messageInputDom = document.querySelector('#chat-message-input');
    const message = messageInputDom.value;
    if (message!=='') {
        socket.send(JSON.stringify({
          'message': message
        }));
        appendMessage(userName, "right", message);
        messageInputDom.value = '';
    } else {
        alert('Please type a message');
    }
};

document.querySelector('#chat-message-input').focus();
document.querySelector('#chat-message-input').onkeyup = function(e) {
    if (e.keyCode === 13) {  // enter, return

        document.querySelector('#chat-message-submit').click();
    }
};

function appendMessage(name, side, text) {
    const msgHTML = `
      <div class="msg ${side}-msg">

        <div class="msg-bubble">
          <div class="msg-info">
            <div class="msg-info-name">${name}</div>
          </div>

          <div class="msg-text">${text}</div>
        </div>
      </div>
    `;

    message_form.insertAdjacentHTML("beforeend", msgHTML);
    message_form.scrollTop += 500;
  }
