#!/usr/bin/env python
"""
A very simple commando example.
This does NOT use protocols and in that way is a BAD example
"""

import sys
import time

from serial import Serial

# play with the path so we can import pycommando even if it's nto installed
try:
    import pycommando
except ImportError:
    sys.path.append('../../')
    import pycommando

# connect to the serial port
port = Serial('/dev/ttyACM0', 9600)
# if this is an arduino, reset it and wait
#time.sleep(1)  # wait for arduino
#port.setDTR(level=0)
#time.sleep(1)

# create our stream handler
com = pycommando.Commando(port)


# define a default message callback
# this will get called whenever a message is received
def show(bs):
    print("Arduino said: %s" % bs)


# register the callback
com.register_message_callback(show)

# send a message to the arduino
print("Computer saying: hi")
com.send_message("hi")

# wait a bit
time.sleep(0.1)
# handle the stream
while port.inWaiting():
    com.handle_stream()
