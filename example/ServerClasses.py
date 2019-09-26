import threading
import sys
sys.path.append('../')
from webthing import (MultipleThings, Property, Thing, Value, WebThingServer)
import logging
logging.getLogger('tornado.access').disabled = True


class UnityLight(Thing):
    def get_name(self):
        return self.name
    def __init__(self, name):
        self.name = name
        Thing.__init__(self, 'urn:dev:ops:'+name, name, ['OnOffSwitch', 'Light'], 'A virtual Unity light')
        self.add_property(
            Property(self,
                     'on',
                     Value(True, lambda v: print('On-State is now', v)),
                     metadata={
                         '@type': 'OnOffProperty',
                         'title': 'On/Off',
                         'type': 'boolean',
                         'description': 'Whether the lamp is turned on',
                     }))

        self.add_property(
            Property(self,
                     'brightness',
                     Value(50, lambda v: print('Brightness is now', v)),
                     metadata={
                         '@type': 'BrightnessProperty',
                         'title': 'Brightness',
                         'type': 'integer',
                         'description': 'The level of light from 0-100',
                         'minimum': 0,
                         'maximum': 100,
                         'unit': 'percent',
                     }))
class UnityButton(Thing):
    """A humidity sensor which updates its measurement every few seconds."""
    def get_name(self):
        return self.name
    def __init__(self, name):
        self.name = name
        Thing.__init__(
            self,
            'urn:dev:ops:my-humidity-sensor-'+name,
            name,
            ['OnOffSwitch'],
            'A web button'
        )

        self.add_property(
            Property(self,
                     'on',
                     Value(True, lambda v: print('On-State is now', v)),
                     metadata={
                         '@type': 'OnOffProperty',
                         'title': 'On/Off',
                         'type': 'boolean',
                         'description': 'Whether the lamp is turned on',
                     }))

class QuestionThing(Thing):
    def get_name(self):
        return self.name
    def __init__(self, name):
        self.name = name
        Thing.__init__(self, 'urn:dev:ops:question-thing-'+name, name, ['OnOffSwitch'],'A web button')

        self.add_property(
            Property(self,
                     'question',
                     Value("Current Question"),
                     metadata={
                         'title': 'question',
                         'type': 'string',
                         'description': 'String test',
                     }))
        self.add_property(
            Property(self,
                     'answer1',
                     Value("Answer Choice One"),
                     metadata={
                         'title': 'answer1',
                         'type': 'string',
                         'description': 'String test',
                     }))
        self.add_property(
            Property(self,
                     'answer2',
                     Value("Answer Choice Two"),
                     metadata={
                         'title': 'answer2',
                         'type': 'string',
                         'description': 'String test',
                     }))
        self.add_property(
            Property(self,
                     'answer3',
                     Value("Answer Choice Three"),
                     metadata={
                         'title': 'answer3',
                         'type': 'string',
                         'description': 'String test',
                     }))
        self.add_property(
            Property(self,
                     'answer4',
                     Value("Answer Choice Four"),
                     metadata={
                         'title': 'answer4',
                         'type': 'string',
                         'description': 'String test',
                     }))
        self.add_property(
            Property(self,
                     'correctcount',
                     Value(0),
                     metadata={
                         'title': 'correctcount',
                         'type': 'int',
                         'description': 'String test',
                     }))
        self.add_property(
            Property(self,
                     'chosenanswer',
                     Value("None"),
                     metadata={
                         'title': 'chosenanswer',
                         'type': 'string',
                         'description': 'String test',
                     }))
        self.add_property(
            Property(self,
                     'newquestion',
                     Value(False),
                     metadata={
                         'title': 'newquestion',
                         'type': 'boolean',
                         'description': 'String test',
                     }))


class Server():
    def __init__(self):
        print("Server Reader to Start")
        self.server = None
        self.x = None
        self.started = False

    def start(self, devices):
        print("Initliazing and Starting Server")
        self.server = WebThingServer(MultipleThings(devices, 'UnityDevices'), port=8888)
        self.x = threading.Thread(target=self.server.start)
        self.x.daemon = True
        self.x.start()
        self.started = True

    def stop(self):
        print("Server closing")
        self.server.stop()
        self.started = False
