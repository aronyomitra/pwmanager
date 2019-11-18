import os
key_file = r'data\key'
data_file = r'data\data.txt'
exists = True
try:
    file = open (data_file, 'r')
except FileNotFoundError:
    exists = False
    os.mkdir('data')
    file = open (data_file, 'w')
    file.write("fb:name@gmail.com,password\n")
    file.write("gmail:username,password")
    file.close()
    print ("Created new file!")

    #If we ever need to distinguish if the data is currently encrypted or not, this can act like a convenient flag
    #All we have to do is read the key value from the file and if it is b'' then it is not encrypted
    with open (key_file, 'wb') as f:
        f.write(b'')

if exists == True:
    print ("File already exists!")
    print ("Make sure to follow the format:")
    print ("account:username,password")
    file.close()
