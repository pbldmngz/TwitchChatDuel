#!usr/bin/python3

import socket
import time
import re
from whatToDo import whatToDo
from twitchSocket import twitchSocket, initData

def mainProgram(ch, tk):
    initData(ch, tk)
    s, _ = twitchSocket()

    connected = False
    run = True

    while run:
        response = s.recv(2048).decode("utf-8")
        if response == "PING :tmi.twitch.tv\r\n":
            s.send("PONG :tmi.twitch.tv\r\n".encode("utf-8"))
            print('Pong')
        else:
            username = re.search(r"\w+", response).group(0)
            CHAT_MSG = re.compile(r"^:\w+!\w+@\w+\.tmi\.twitch\.tv PRIVMSG #\w+ :")
            
            message = CHAT_MSG.sub("", response).rstrip('\n')

            if message[0] == "!": 
                whatToDo(message)

            if 'End of /NAMES list' in message:
                connected = True
                print('Listening to stream chat')


            if connected == True:  
                if 'End of /NAMES list' in message:
                    pass
                else:
                    #pass
                    print(username.title() + ':', message)

            #so we don't send messages too fast
            time.sleep(0.25)

mainProgram("spe...", "oauth:24l...")