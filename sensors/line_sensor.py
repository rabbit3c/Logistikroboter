from gpiozero import InputDevice


sensor_left = InputDevice(14)
sensor_right = InputDevice(15)
state = "normal"


# Left line sensor, returns true if sensor detects line
def line_left():
    return not sensor_left.is_active


# Right line sensor, returns true if sensor detects line
def line_right():
    return not sensor_right.is_active