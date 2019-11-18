import getpass
import login
import hashlib
import encrypt as enc

config_file = r'config.ini'
conf = {}
with open (config_file, 'r') as f:
    for line in f:
        (key, val) = line.split('=')
        conf[key] = val.strip()

GLOBAL_APP_PW = conf['passkey']

# There is a global password that is asked on opening, and it is required to proceed further
# This has been added for security, as otherwise anyone on the machine can login for free
app_pw = getpass.getpass("Enter password to access app: ")
hash = hashlib.md5(app_pw.encode('utf-8')).hexdigest()
if hash != GLOBAL_APP_PW:
    print ('Wrong password. Exiting')
    exit()

if enc.getKey() == b'':
    initiallyEncrypted = False
else:
    initiallyEncrypted = True
    enc.decrypt()

account = input ("Enter account: ")

file = open(r"data\data.txt", 'r')
data = file.readlines()
file.close()

if initiallyEncrypted:
    enc.createNewKey()
    enc.encrypt()

accExists = False;
for line in data:
    temp = line.split(':')
    acc = temp[0]
    creds = temp[1]

    if acc == account:
        credList = creds.split(',')
        accExists = True;

if accExists == False:
    print ("Account does not exist")
    exit();

login.login (account, credList)
