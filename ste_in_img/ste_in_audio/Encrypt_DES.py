import base64
import hashlib
from Crypto.Cipher import DES
# Mã hóa DES bằng password md5
def encryptDES(plain_text, pwd):
    try:
        salt = '\x28\xAB\xBC\xCD\xDE\xEF\x00\x33'
        key = pwd + salt
        m = hashlib.md5(key.encode())
        key = m.digest()
        (dk, iv) =(key[:8], key[8:])
        crypter = DES.new(dk, DES.MODE_CBC, iv)

        print("The plain text is : ",plain_text)
        plain_text = pad(plain_text)
        ciphertext = crypter.encrypt(plain_text.encode())
        encode_string= base64.b32encode(ciphertext)
        print("The encoded string is : ",encode_string)
        return encode_string.decode()
    except:
        print(Exception)

def pad(text):
    while(len(text) % 8 != 0):
        text += ' '
    return text

# Giải mã DES bằng password md5
def decryptDES(cipher_text,pwd):
    try:
        salt = '\x28\xAB\xBC\xCD\xDE\xEF\x00\x33'
        key = pwd + salt
        m = hashlib.md5(key.encode())
        key = m.digest()
        (dk, iv) =(key[:8], key[8:])
        crypter = DES.new(dk, DES.MODE_CBC, iv)

        print("The ecrypted string is : ",cipher_text)
        cipher_text = base64.b32decode(cipher_text)
        decrypted_string = crypter.decrypt(cipher_text)
        print("The decrypted string is : ",decrypted_string)
        return decrypted_string.decode()
    except:
        print(Exception)

# msg = encryptDES("lenh ha bao long","8023")
# pl = decryptDES(msg.encode(),"8023")
# print(pl)