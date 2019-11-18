from cryptography.fernet import Fernet

key_file = r'data\key'
data_file = r'data\data.txt'
def createNewKey():
    key = Fernet.generate_key()
    print (key)
    with open (key_file, 'wb') as f:
        f.write(key)

def getKey():
    with open (key_file, 'rb') as f:
        key = f.read()
    return key

def encrypt():
    key = getKey()
    fnt = Fernet(key)
    with open (data_file, 'rb') as f:
        data = f.read()

    encrypted = fnt.encrypt(data)

    with open (data_file, 'wb') as f:
        f.write(encrypted)

def decrypt():
    key = getKey()
    fnt = Fernet(key)
    with open (data_file, 'rb') as f:
        data = f.read()

    decrypted = fnt.decrypt(data)

    with open (data_file, 'wb') as f:
        f.write(decrypted)

    with open (key_file, 'wb') as f:
        f.write(b'')
