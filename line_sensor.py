from gpiozero import InputDevice
from serial_communication import *

sensor_left = InputDevice(14)
sensor_right = InputDevice(15)
state = "normal"

def line_left():
    return not sensor_left.is_active

def line_right():
    return not sensor_right.is_active