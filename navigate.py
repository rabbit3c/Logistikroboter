from sensors.line_sensor import *
from serial_communication import *
from path import Path
import robot
import sensors.points_counter as points_counter


states = ["intersection", "line_left", "line_right", "normal"]


def navigate(path):
    left = line_left()
    right = line_right()
    finished = False

    if left and right:
        if check_if_changed(0):
            print("Intersection detected")
            navigate_intersection(path)
    elif left:
        finished = points_counter.check_sensor(path, True)
        if check_if_changed(1):
            # print("Line detected on the left")
            robot.left()
    elif right:
        finished = points_counter.check_sensor(path, True)
        if check_if_changed(2):
            # print("Line detected on the right")
            robot.right()
    else:
        finished = points_counter.check_sensor(path, False)
        if check_if_changed(3):
            send_command("forward")
            robot.forward()

    if finished:
        send_command("stop")
        return


def navigate_intersection(path: Path):
    robot.stop()

    direction = path.next()
    match direction:
        case path.right:
            print("Turning right...\n")
            robot.turn_right(path)
        case path.left:
            print("Turning left...\n")
            robot.turn_left(path)
        case path.forward:
            print("Continuing straight...\n")
            robot.forward()
            sleep(0.5)
            path.check_path_done()
        case _:
            robot.stop()


def check_if_changed(i): # i -> index in states
    global state

    if state == states[i]:
        return False
    state = states[i]
    return True
