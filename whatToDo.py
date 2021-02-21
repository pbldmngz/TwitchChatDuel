from pynput.keyboard import Key, Controller as KeyboardController
from pynput.mouse import Button, Controller as MouseController

from time import sleep
from twitchSocket import sendMSG

kb = KeyboardController()
ms = MouseController()

shifting = False
crouching = False
adsing = False
multiplier = 1

####################################

def sendMessage(message):
    sendMSG(message)

# Determine wich function to use
def whatToDo(cmd):
    cmd = cmd[:-1].split(" ")
    print(cmd)

    # Soy vago como para hacer una mejor implementación de esto
    try:
        # Mouse
        if cmd[0] == "!ms": # move mouse
            moveMouse(cmd[1], 0)
            moveMouse(0, cmd[2])
        elif cmd[0] == "!ads": # mouse button 2
            ads()
        elif cmd[0] == "!fire": # mouse button 1
            fire()

        # Keyboard Basic WASD
        elif cmd[0] == "!fw": # W
            forward(cmd[1])
        elif cmd[0] == "!bw": # S
            backward(cmd[1])
        elif cmd[0] == "!lt": # A
            left(cmd[1])
        elif cmd[0] == "!rt": # D
            right(cmd[1])

        # Extra Keyboard
        elif cmd[0] == "!ult": # X
            ult()
        elif cmd[0] == "!jump": # SPACE
            jump()
        elif cmd[0] == "!cruch": # CTRL
            crouch()
        elif cmd[0] == "!shift": # Toggle Shift
            shift()

        # Change gun
        elif cmd[0] == "!gun1": # 1
            mainGun()
        elif cmd[0] == "!gun2": # 2
            secGun()
        elif cmd[0] == "!gun3": # 3
            knife()

        # Se confundió el comando
        else: 
            print("something is wrong")
            sendMessage("'{}' wrong command format".format(" ".join(cmd)))
    except Exception as e: 
        print("something is wrong")
        print(e)
        sendMessage("'{}' wrong command format".format(" ".join(cmd)))
        

# MOUSE
def pressMouseBT(LoR):
    global ms, adsing

    if LoR == "left":
        ms.press(Button.left)
        sleep(0.5)
        ms.release(Button.left)
    else:
        if adsing == False:
            ms.press(Button.right)
            adsing = True
        else:
            ms.release(Button.right)

def moveMouse(x, y):
    global ms, multiplier

    x, y = multiplier*int(x), multiplier*int(y)

    ms.move(x, y)

def ads():
    pressMouseBT("right")

def fire():
    pressMouseBT("left")

# Press Keyboard key
def pressKey(key, time = 0.75):
    global kb

    kb.press(key)
    sleep(int(time)/4)
    kb.release(key)

# WASD
def forward(t):
    pressKey("W", t)

def left(t):
    pressKey("A", t)

def right(t):
    pressKey("R", t)

def backward(t):
    pressKey("S", t)

# Extra KEYBOARD
def mainGun():
    pressKey("1")

def secGun():
    pressKey("2")

def knife():
    pressKey("3")

def ult():
    pressKey("X")

def jump():
    pressKey(Key.space)

def crouch():
    global kb, shifting

    if crouching == False:
        kb.press(Key.ctrl)
        crouching = True
    else:
        kb.release(Key.ctrl)

def shift():
    global kb, shifting

    if shifting == False:
        kb.press(Key.shift)
        shifting = True
    else:
        kb.release(Key.shift)
    

########
# ADD TANDEM MODE
# TRY TO MOVE IN DEGREES INSTEAD OF ARBITRARY NUMBERS