import pyperclip, time
from pynput.keyboard import Key, Controller

keyboard = Controller()
def login(acc, credList):
    if credList[-1][-1] == '\n':
        credList[-1] = credList[-1][0:-1]

    #Checking acc against preset accounts
    if acc == 'fb':
        time.sleep(3)
        keyboard.type(credList[0] + '\t' + credList[1] + '\r')
    elif acc == 'gmail':
        time.sleep(3)
        keyboard.type(credList[0] + '\r')
        time.sleep(2)
        keyboard.type(credList[1] + '\r')
    elif acc == 'steam':
        time.sleep(3)
        keyboard.type(credList[0] + '\t' + credList[1] + '\r')
