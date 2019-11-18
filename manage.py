import encrypt as enc
key_file = r'data/key'
data_file = r'data/data.txt'

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
        enc.createNewKey()
        enc.encrypt()
        print ("Done.")
    else:
        print ("Files are already encrypted. Wouldn't want to overdo it :3")

def op3():
    key = enc.getKey()
    if key == b'':
        enc.createNewKey()
        enc.encrypt()
    else:
        enc.decrypt()
        enc.createNewKey()
        enc.encrypt()

    print ("Done.")


print ("\nFile Management Section")
print ("-----------------------\n")
print ("1) Decrypt all files")
print ("2) Encrypt all files")
print ("3) Re-encrypt everything with new key")

x = input ("\nEnter choice: ")
if x == '1':
    op1()
elif x == '2':
    op2()
elif x == '3':
    op3()
else:
    print ('Invalid input')
