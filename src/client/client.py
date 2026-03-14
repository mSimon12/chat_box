import asyncio
import websockets
import threading
from queue import Queue
from typing import List

from .message import ChatMessage


class ChatClient:
    def __init__(self, uri: str = "ws://localhost:8000/ws"):
        self._uri = uri
        self._username = None

        self._receive_queue: Queue[str] = Queue()
        self._send_queue: Queue[str] = Queue()
        self._connected_flag = False

    async def session(self):
        async with websockets.connect(self._uri) as websocket:
            while self._connected_flag:
                # Check for messages to send
                if not self._send_queue.empty():
                    msg_content = self._send_queue.get()
                    new_message = ChatMessage(self._username, msg_content)

                    await websocket.send(new_message.encrypt())
                # Try to receive with timeout
                try:
                    message = await asyncio.wait_for(websocket.recv(), timeout=0.1)
                    recv_message = ChatMessage.decrypt(message)
                    if recv_message.user != self._username:
                        self._receive_queue.put(recv_message.content)

                except asyncio.TimeoutError:
                    pass

    def connect(self, username):
        self._username = username
        self._connected_flag = True
        thread = threading.Thread(target=lambda: asyncio.run(self.session()), daemon=True)
        thread.start()

    def disconnect(self):
        self._connected_flag = False
        self._username = None

    def send_message(self, new_message: str):
        self._send_queue.put(new_message)

    def get_messages(self) -> List[str]:
        messages = []
        while not self._receive_queue.empty():
            messages.append(self._receive_queue.get())
        return messages