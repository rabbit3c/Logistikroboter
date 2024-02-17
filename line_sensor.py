from gpiozero import InputDevice
from serial_communication import *

sensor_left = InputDevice(14)
sensor_right = InputDevice(15)
state = "normal"

def line_left():
    return not sensor_left.is_active

def line_right():
    return not sensor_right.is_active

def update_state():
    left = line_left()
    right = line_right()

    if left and right:
        if check_if_changed(0):
            print("Intersection detected")
            send_command("stop")
    elif left:
        if check_if_changed(1):
            print("Line detected on the left")
            send_command("left")
    elif right:
        if check_if_changed(2):
            print("Line detected on the right")
            send_command("right")
    else:
        if check_if_changed(3):
            send_command("forward")

def check_if_changed(i): #index in states
    states = ["intersection", "line_left", "line_right", "normal"]
    global state

    if state == states[i]:
        return False
    state = states[i]
    return True
