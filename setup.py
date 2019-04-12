import os
exists = os.path.isFile(r"data\data.txt")
if exists == False:
    file = open (r"data\data.txt", 'w')
    file.write("fb:name@gmail.com,password")
    file.write("gmail:username,password")
    file.close()
    print ("Created new file!")
else:
    print ("File already exists!")
    print ("Make sure to follow the format:")
    print ("account:username,password")

file.close()
