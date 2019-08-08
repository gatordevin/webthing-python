Implementation of an HTTP `Web Thing <https://iot.mozilla.org/wot/>`_. This library is compatible with Python 3.4+. This code is a fork of the main webthing-python branch https://github.com/mozilla-iot/webthing-python.

This fork is designed to connect to a socket client and recieve commands. Was designed for the specific use case of creating virtual IoT devices from Unity and having the webthing-python code dynamicially start and stop the server as devices are added.

Installation
============

``python-webthing`` can be installed via ``git``, as such:

.. code:: shell

  $ git clone https://github.com/gatordevin/webthing-python.git

Running the Sample
==================

.. code:: shell

  $ cd webthing-python/example
  $ python3 UnityProxy.py

Once the code is started it will continue to run and open a server scoekt on port 2000. The next step is to write a coket client that connects to the ip address of the computer the code is running on at port 2000. The server will then wait for data from the client.

Expected Packet Structure
======================
The server is listening for a few specefic command strings.

``Start``

Upon receiving Start as a string over the socket it will then wait for a JSON string to be sent by the client immediatly after.
JSON Structrure is as follows:
{"UnityLight": ["LightOne", "LightTwo"...,"LightHundred"], "UnityButton": ["ButtonOne", "ButtonTwo"...,"ButtonHundred"]}

Once it receives this JSON string it will decode it determine how many of each device you want and the name of each and then start the IoT Device Server with all of these devices. They will then be avaiable upon search from the Mozilla Gateway.

``Data``

Upon recieving Data as a string over the socket it will then create a JSON string to be sent to the client that has all the device names as keys, with another JSON object as their value which contains all the property names and values fro the object.

``Stop``

Upon recieving Stop as a string over the socket it will shut down the server. Currently the Unity code sends this when the game is stopped this prepares the python code for new devices and possibly a new Unity client.
