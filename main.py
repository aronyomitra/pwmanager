import getpass
import login

GLOBAL_APP_PW = "pass"

# There is a global password that is asked on opening, and it is required to proceed further
# This has been added for security, as otherwise anyone on the machine can login for free 
app_pw = getpass.getpass("Enter password to access app: ")
if app_pw != GLOBAL_APP_PW:
    print ('Wrong password. Exiting')
    exit()

account = input ("Enter account: ")

file = open(r"data\data.txt", 'r')
data = file.readlines()
file.close()

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
