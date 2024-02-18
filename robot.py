from serial_communication import *
from line_sensor import *

def init():
    communication_test()
    set_speed(100)

def stop():
    send_command("stop")

def forward():
    send_command("forward")

def backward():
    send_command("backwward")

def right():
    send_command("right")

def left():
    send_command("left")

def turn_right():
    forward()
    sleep(0.2)
    stop()
    send_command("turn_right")
    sleep(2)
    while not line_right():
        pass
    while line_right():
        pass

def turn_left():
    forward()
    sleep(0.2)
    stop()
    send_command("turn_left")
    sleep(2)
    while not line_left():
        pass
    while line_left():
        pass

