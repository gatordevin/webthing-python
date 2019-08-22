import socket
import select
from threading import Thread
import sys
HOST = '127.0.0.1'
PORT = 2000

class ClientHandler(Thread):
    def __init__(self,conn,port):
        Thread.__init__(self)
        self.conn = conn
        self.port = port
        print("Thread started with " + str(self.port))

    def run(self):
        while True:
            data = self.conn.recv(1024)
            if not data:
                print('Thread Closing')
                sys.exit()
                break
            data = data.decode("utf-8")
            print(str(self.port) + " says " + data)

class ClientListener(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.bind((HOST, PORT))

    def run(self):
        while True:
            self.s.listen(5)
            (c, (ip,port)) = self.s.accept()
            ClientHandlerClass = ClientHandler(c,port)
            ClientHandlerClass.start()

ClientListenerClass = ClientListener()
ClientListenerClass.start()
while True:
    pass
