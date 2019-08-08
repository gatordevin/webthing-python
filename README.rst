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

Upon recieving Start as a string over the socket it will then wait for a JSON string to be sent by the client immediatly after.
JSON Structrure is as follows:
{
  "UnityLight": ["LightOne", "LightTwo"...,"LightHundred"], 
  "UnityButton": ["ButtonOne", "ButtonTwo"...,"ButtonHundred"]
}

``Data``

``Stop``

