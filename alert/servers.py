import socket, traceback
import winsound

host = ''
port = 51423

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((host, port))
s.listen(1)
print "done"

while 1:
    #when connect error happen, skip the error
    try:
        ClientSock, ClientAddr = s.accept()
    except KeyboardInterrupt:
        raise
    except:
        traceback.print_exc()
        continue

    #Get informaion form client and reply
    try:
        print "Get connect from ", ClientSock.getpeername()
        data = ClientSock.recv(1024)
        if data =="baojing":
            winsound.PlaySound("alert.wav", winsound.SND_FILENAME)


        #while 1:
         #   str = raw_input("What you want to say:")
        #    ClientSock.sendall(str)
         #   ClientSock.sendall('\n')
    except (KeyboardInterrupt ,SystemError):
        raise
    except:
        traceback.print_exc()

    #Clocs socket
    try:
        ClientSock.close()
    except KeyboardInterrupt:
        raise
    except:
        traceback.print_exc()
