from example import ServerClasses
from time import sleep
DeviceList = []
server = ServerClasses.Server()

DeviceList.append(ServerClasses.QuestionThing("RedQuestion"))
server.start(DeviceList)

while True:
    DeviceList[0].set_property("question", "Which type of energy is needed to cut a piece of wood into smaller pieces with a saw?")
    sleep(5)
    DeviceList[0].set_property("question","Uh")
    sleep(5)
