import socket
import select
from threading import Thread
import sys
import tornado.ioloop
import tornado.web
import json
import ServerClasses

clients = []
IoTdevices = []
DeviceList = []
started = False

### SOCKET HANDLER CLASSES
class ClientHandler(Thread):
    global IoTdevices
    def __init__(self,conn,port):
        Thread.__init__(self)
        self.conn = conn
        self.port = port
        self.clientDevice = []
        clients.append(str(self.port))
        print("Thread started with " + str(self.port))

    def run(self):
        while True:
            data = self.conn.recv(1024)
            if not data:
                print('Thread Closing')
                clients.remove(str(self.port))
                sys.exit()
            data = data.decode("utf-8")
            jsonData = json.loads(data)


            for deviceType, devices in jsonData.items():
                for device in devices:
                    self.clientDevice.append(device)
                    if not device in IoTdevices:
                        IoTdevices.append(device)
                    try:
                        DeviceList.append(getattr(ServerClasses, deviceType)(device))
                    except NameError:
                        pass

class ClientListener(Thread):
    def __init__(self, HOST, PORT):
        Thread.__init__(self)
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.bind((HOST, PORT))

    def run(self):
        while True:
            self.s.listen(5)
            (c, (ip,port)) = self.s.accept()
            ClientHandlerClass = ClientHandler(c,port)
            ClientHandlerClass.start()



### TORNADO HANDLER CLASSES WEBPAGE
class MainHandler(tornado.web.RequestHandler):
    global clients
    global IoTdevices
    def get(self):
        self.render("template.html", title="Proxy Interface", clients=clients, IoTDevices=IoTdevices )

class StopServerHandler(tornado.web.RequestHandler):

    def get(self):
        serverStarter(False)

class StartServerHandler(tornado.web.RequestHandler):

    def get(self):
        serverStarter(True)

def make_app():
    return tornado.web.Application([
            (r"/", MainHandler),
            (r"/stopIoT", StopServerHandler),
            (r"/startIoT", StartServerHandler)
        ])
def serverStarter(start):
    global started
    global DeviceList
    if(start):
        if not started:
            print(DeviceList)
            server.start(DeviceList)
            started = True
    else:
        if started:
            server.stop()
            started = False



### MAIN CODE
if __name__ == "__main__":
    HOST = '127.0.0.1'
    PORT = 2000
    ClientListenerClass = ClientListener(HOST, PORT)
    ClientListenerClass.start()
    app = make_app()
    app.listen(8000)
    server = ServerClasses.Server()
    tornado.ioloop.IOLoop.current().start()
