from line_sensor import *
from serial_communication import *
import robot
import points_counter

def navigate(path):
    left = line_left()
    right = line_right()
    finished = points_counter.check_sensor(path)

    if finished:
        send_command("stop")
        return

    if left and right:
        if check_if_changed(0):
            print("Intersection detected")
            navigate_intersection(path)
    elif left:
        if check_if_changed(1):
            print("Line detected on the left")
            robot.left()
    elif right:
        if check_if_changed(2):
            print("Line detected on the right")
            robot.right()
    else:
        if check_if_changed(3):
            send_command("forward")
            robot.forward()


def navigate_intersection(path):
    robot.stop()

    direction = path.next()
    match direction:
        case path.right:
            robot.turn_right()
        case path.left:
            robot.turn_left()
        case path.forward:
            robot.forward()
            sleep(0.5)
        case _:
            robot.stop()

    path.check_path_done()


def check_if_changed(i): # i -> index in states
    states = ["intersection", "line_left", "line_right", "normal"]
    global state

    if state == states[i]:
        return False
    state = states[i]
    return True
