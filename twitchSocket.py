import socket

def twitchSocket():
    auth = {
        "server" : 'irc.chat.twitch.tv',
        "port" : 6667,
        "nickname" : "Mergus",
        "token" : "oauth:g61low....",
        "channel" : "spectratd"#"arkhanzu" 
    }

    
    s = socket.socket()
    s.connect((auth["server"], auth["port"]))
    s.send("PASS {}\r\n".format(auth["token"]).encode("utf-8"))
    s.send("NICK {}\r\n".format(auth["nickname"]).encode("utf-8"))
    s.send("JOIN #{}\r\n".format(auth["channel"]).encode("utf-8"))

    return s, auth

def sendMSG(message):
    s, auth = twitchSocket()

    messageTemp = "PRIVMSG #" + auth["channel"] + " :" + message
    s.send(messageTemp.encode() + "\r\n".encode())
    print("Sent: " + messageTemp)