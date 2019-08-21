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

    def run(self):
        while True:
            try:
                ready_to_read, ready_to_write, in_error = select.select([self.conn,], [self.conn,], [], 5)
            except select.error:
                print("Uh")
                self.conn.shutdown(2)
                self.conn.close()
                sys.exit()
            if(len(ready_to_read) > 0):
                data = self.conn.recv(1024)
                #print(str(self.port) + " says: " + data.decode("utf-8"))

class ClientListener(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.bind((HOST, PORT))

    def run(self):
        while True:
            self.s.listen(5)
            (c, (ip,port)) = self.s.accept()
            ClientHandlerClass = ClientHandler(c,ip)
            ClientHandlerClass.start()

ClientListenerClass = ClientListener()
ClientListenerClass.start()
while True:
    pass
