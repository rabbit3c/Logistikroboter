from serial_communication import *
from line_sensor import *


def init():
    communication_test()
    set_speed(95)


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
    #forward()
    #sleep(0.05)
    #stop()
    send_command("turn_right")
    sleep(1)
    while not line_right(): #wait until reaching the line
        pass
    while line_right(): #wait until the line was crossed by the right sensor
        pass


def turn_left():
    #forward()
    #sleep(0.05)
    #stop()
    send_command("turn_left")
    sleep(1)
    while not line_left(): #wait until reaching the line
        pass
    while line_left(): #wait until the line was crossed by the right sensor
        pass

