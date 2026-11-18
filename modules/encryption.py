import secrets
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes

#symmetric encryption
def aes_ed(message):
    key = secrets.token_bytes(32)
    nonce = secrets.token_bytes(12)

    #create encryption and decription objects
    aes = AESGCM(key)

    ciphertext = nonce + aes.encrypt(nonce, message.encode(), None) #convert message to bytes
    plaintext = aes.decrypt(ciphertext[:12], ciphertext[12:], None)

    return key.hex(), ciphertext.hex(), plaintext.decode()

#asymmetric encryption ~ rmr this uses two keys
def rsa_ed(message):
    private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
    public_key = private_key.public_key()

    #encrypting the data
    ciphertext = public_key.encrypt(
        message.encode(),
        padding.OAEP( #adding padding
            mgf = padding.MGF1(algorithm=hashes.SHA256()),
            algorithm = hashes.SHA256(),
            label = None
        )
    )
    #decrypt the data
    plaintext = private_key.decrypt(
        ciphertext,
        padding.OAEP( #adding padding
            mgf = padding.MGF1(algorithm=hashes.SHA256()),
            algorithm = hashes.SHA256(),
            label = None
        )
    )
    return ciphertext.hex(), plaintext.decode()

if __name__ == "__main__":
    print(aes_ed("Hello, AES!"))
    print(rsa_ed("Hello, RSA!"))
