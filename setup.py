import os
exists = True
try:
    file = open ("data\data.txt", 'r')
except FileNotFoundError:
    exists = False
    os.mkdir('data')
    file = open ("data\data.txt", 'w')
    file.write("fb:name@gmail.com,password")
    file.write("gmail:username,password")
    file.close()
    print ("Created new file!")

if exists == True:
    print ("File already exists!")
    print ("Make sure to follow the format:")
    print ("account:username,password")
    file.close()
