import socket
import ServerClasses
import json
from threading import Thread
class MagicLeapHandler(Thread):

    def __init__(self,ip,port,master):
        Thread.__init__(self)
        self.ip = ip
        self.port = port
        self.master = master
        self.team = None
        print("thread init")
        #print "[+] New server socket thread started for " + ip + ":" + str(port)

    def run(self):
        print("Uh")
        DeviceList = []
        if(self.master):
            print("master")
            server = ServerClasses.Server()
            print("Connection With:", self.ip)
            c.sendall(str.encode("waiting"))
            data = c.recv(100)
            data = data.decode("utf-8")
            print(data)
            jsonData = json.loads(data)
            for property, value in jsonData.items():
                if(property == "Color"):
                    self.team = value
            while True:
                data = c.recv(1024)
                if not data:
                    print("disconnect")

                data = data.decode("utf-8")
                if data == "Start":

                    data = c.recv(1024)
                    data = data.decode("utf-8")
                    jsonData = json.loads(data)


                    for deviceType, devices in jsonData.items():
                        for device in devices:
                            try:
                                DeviceList.append(getattr(ServerClasses, deviceType)(device))

                            except NameError:
                                pass
                    server.start(DeviceList)
                    c.sendall(b"Started")

                elif data == "Data":
                    data = {}
                    for device in DeviceList:
                        light = {}
                        data[device.get_name()] = device.get_properties()
                        json_data = json.dumps(data)
                    c.sendall(str.encode(json_data))

                elif data == "Stop":
                    server.stop()
                    DeviceList = []
        else:
            c.sendall(str.encode("running"))
            data = c.recv(1024)
            data = data.decode("utf-8")
            jsonData = json.loads(data)
            for property, value in jsonData.items():
                if(property == "Color"):
                    self.team = value
            while True:
                data = c.recv(1024)

                #if not data:
                #    break

                data = data.decode("utf-8")
                if data == "Data":
                    data = {}
                    for device in DeviceList:
                        light = {}
                        data[device.get_name()] = device.get_properties()
                        json_data = json.dumps(data)
                    c.sendall(str.encode(json_data))


#Optional for running other processes in addition to server code
'''
class NewDeviceHandler(Thread):

    def __init__(self):
        Thread.__init__(self)

    def run(self):
        while True:
            tcpServer.listen(5)
            (conn, (ip,port)) = tcpServer.accept()
            newMagicLeapHandler = MagicLeapHandler(ip,port)
            newMagicLeapHandler.start()
            threads.append(newMagicLeapHandler)

DeviceHandlerThread = NewDeviceHandler()
DeviceHandlerThread.start()
while True:
    print("Loop")
'''
port = 2000
s = socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(('', port))
print("Bound to Port:", port)
s.listen(5)
(c, (ip,port)) = s.accept()
newMagicLeapHandler = MagicLeapHandler(ip,port,True)
newMagicLeapHandler.start()
while True:
    s.listen(5)
    (conn, (ip,port)) = s.accept()
    newMagicLeapHandler = MagicLeapHandler(ip,port,False)
    newMagicLeapHandler.start()
    threads.append(newMagicLeapHandler)

s = socket.socket()
