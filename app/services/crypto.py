import base64
import hashlib
import secrets
from cryptography.hazmat.primitives.ciphers.aead import AESGCM

class CryptoService:
    
    @staticmethod
    def generate_room_key() -> str:
        key = secrets.token_bytes(32)
        return base64.urlsafe_b64encode(key).decode()
    
    @staticmethod
    def derive_key_from_room(room_id: str, salt: str = "mlichat") -> bytes:
        key = hashlib.pbkdf2_hmac(
            "sha256",
            room_id.encode(),
            salt.encode(),
            100000,
            dklen=32
        )
        return key
    
    @staticmethod
    def encrypt_message(message: str, key: bytes) -> str:
        aesgcm = AESGCM(key)
        nonce = secrets.token_bytes(12)
        ciphertext = aesgcm.encrypt(nonce, message.encode(), None)
        encrypted_data = nonce + ciphertext
        return base64.urlsafe_b64encode(encrypted_data).decode()
    
    @staticmethod
    def decrypt_message(encrypted_message: str, key: bytes) -> str:
        try:
            encrypted_data = base64.urlsafe_b64decode(encrypted_message.encode())
            nonce = encrypted_data[:12]
            ciphertext = encrypted_data[12:]
            aesgcm = AESGCM(key)
            plaintext = aesgcm.decrypt(nonce, ciphertext, None)
            return plaintext.decode()
        except Exception:
            return "[Decryption Failed]"
    
    @staticmethod
    def generate_room_id() -> str:
        return secrets.token_urlsafe(8)


crypto_service = CryptoService()
