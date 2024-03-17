from passlib.context import CryptContext
from cryptography.fernet import Fernet

from config import config


def generate_key() -> bytes:
    return Fernet.generate_key()


class Crypt:
    def __init__(self, key:bytes|str = config.get("CRYPT_KEY", generate_key())) -> None:
        self.key = key
        self.fernet = Fernet(key=self.key)
    
    @property
    def get_key(self) -> str:
        return self.key if isinstance(self.key, str) else self.key.decode()

    def encrypt(self, data:bytes|str) -> bytes:
        return self.fernet.encrypt(data=data.encode() if isinstance(data, str) else data)
    
    def decrypt(self, token:bytes|str) -> str:
        return self.fernet.decrypt(token=token).decode()


class Hash:
    def __init__(self) -> None:
        self.context = CryptContext(schemes=["bcrypt"], deprecated="auto")
    
    def bcrypt(self, secret: bytes|str) -> str:
        return self.context.hash(secret=secret)
    
    def verify_secret(self, secret: bytes|str, hashed_secret: bytes|str) -> bool:
        return self.context.verify(secret=secret, hash=hashed_secret)
