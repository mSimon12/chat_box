from dataclasses import dataclass 
import base64

@dataclass
class ChatMessage:
    user: str
    content: str

    def __init__(self, user_id: str, content: str):
        self.user = user_id
        self.content = content
    
    def encrypt(self) -> bytes:
        combined = f"{self.user}|{self.content}"
        return base64.b64encode(combined.encode())

    @classmethod
    def decrypt(cls, encoded_message: bytes) -> "ChatMessage":
        decoded = base64.b64decode(encoded_message).decode()
        user_id, content = decoded.split("|", 1)
        return cls(user_id=user_id, content=content)
