from gpiozero import InputDevice

sensor_left = InputDevice(14)
sensor_right = InputDevice(15)

def line_left():
    if sensor_left.is_active:
        print("Line detected on the left")
        return True
    return False

def line_right():
    if sensor_right.is_active:
        print("Line detected on the right")
        return True
    return False

