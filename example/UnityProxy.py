import socket
import ServerClasses
import json
s = socket.socket()

port = 2000
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(('', port))
print("Bound to Port:", port)

s.listen(5)
print("Listening")

server = ServerClasses.Server()
while True:
    c, addr = s.accept()
    print("Connection With:", addr)
    DeviceList = []
    with c:
        while True:
            data = c.recv(1024)

            if not data:
                break

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
