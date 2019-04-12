import getpass
import login

GLOBAL_APP_PW = "passkey"

app_pw = getpass.getpass("Enter password to access app: ")
if app_pw != GLOBAL_APP_PW:
    print ('Wrong password. Exiting')
    exit()

account = input ("Enter account: ")

file = open(r"data\data.txt", 'r')
data = file.readlines()

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
