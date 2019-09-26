import socket
import time
HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 2000        # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b'{"QuestionThing":["RedQuestionThing"]}')
    data = s.recv(1024)
    while True:
        None
        #s.sendall(b'set')
        #data = s.recv(1024)
        #data = data.decode("utf-8")
        #if(data == "ready"):
        #    s.sendall(b'{"BaseStationLightThree": {"on": true, "brightness": 62}}')
        #    data = s.recv(1024)
        #    data = data.decode("utf-8")

#print('Received', repr(data))
