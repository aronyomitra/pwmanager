import encrypt as enc
import hashlib

key_file = r'data/key'
data_file = r'data/data.txt'
config_file = r'config.ini'

def op1():
    key = enc.getKey()
    if key != b'':
        enc.decrypt()
        print ("Done.")
    else:
        print ("Files are already decrypted. Enjoy!")

def op2():
    key = enc.getKey()
    if key == b'':
        print ("The key is " + str(enc.createNewKey()))
        enc.encrypt()
        print ("Done.")
    else:
        print ("Files are already encrypted. Wouldn't want to overdo it :3")

def op3():
    key = enc.getKey()
    if key == b'':
        print ("The key is " + str(enc.createNewKey()))
        enc.encrypt()
    else:
        enc.decrypt()
        print ("The key is " + str(enc.createNewKey()))
        enc.encrypt()

    print ("Done.")

def op4():
    flag = False
    while flag == False:
        passkey = input("Enter a password (no spaces): ")
        passkey = passkey.strip()
        if ' ' in passkey:
            print ("NO SPACES!")
        else:
            flag = True

    with open (config_file, 'w') as f:
        newHash = hashlib.md5(passkey.encode('utf-8')).hexdigest()
        f.write('passkey=' + newHash)

    print ('Done.')
print ("\nFile Management Section")
print ("-----------------------\n")
print ("1) Decrypt all files")
print ("2) Encrypt all files")
print ("3) Re-encrypt everything with new key")
print ("4) Change global passkey")

x = input ("\nEnter choice: ")
if x == '1':
    op1()
elif x == '2':
    op2()
elif x == '3':
    op3()
elif x == '4':
    op4()
else:
    print ('Invalid input')
