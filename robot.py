from serial_communication import *
from sensors.line_sensor import *
import sensors.points_counter as points_counter


def init():
    communication_test()


def stop():
    send_command("stop")


def forward():
    send_command("forward")


def backward():
    send_command("backward")


def right():
    send_command("right")


def left():
    send_command("left")


def turn_right(path):
    forward()
    sleep(0.1)

    send_command("turn_right")
    sleep(0.3)

    while not line_right(): # wait until reaching the line
        pass

    path.check_path_done() # check if points need to be counted

    while line_right(): # wait until the line was crossed by the right sensor
        if points_counter.check_sensor(path): #start to count points if needed, exit if arrived at destination
            return
        pass


def turn_left(path):
    forward()
    sleep(0.05)

    send_command("turn_left")
    sleep(0.3)

    path.check_path_done() # check if points need to be counted

    while not line_left(): # wait until reaching the line
        if points_counter.check_sensor(path): #start to count points if needed, exit if arrived at destination
            return
        pass

    while line_left(): # wait until the line was crossed by the right sensor
        if points_counter.check_sensor(path): #start to count points if needed, exit if arrived at destination
            return
        pass

