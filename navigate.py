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
    
    # if both sensor detect a line, navgigate this interserction
    if left and right: 
        if check_if_changed(0):
            print("Intersection detected")
            navigate_intersection(path)

    # if the left sensor detects the line and the point counting sensor isn't on a point, turn left
    elif left and not points_counter.state:
        if check_if_changed(1):
            robot.left()
        finished = points_counter.check_sensor(path)

    # if the right sensor detects the line and the point counting sensor isn't on a point, turn right
    elif right and not points_counter.state:
        if check_if_changed(2):
            robot.right()
        finished = points_counter.check_sensor(path, backwards=True) # if the robot turns right, the right side of the robot, where the sensor is located, goes backwards

    # if the no sensor detects a line go straight
    else:
        if check_if_changed(3):
            send_command("forward")
            robot.forward()
        finished = points_counter.check_sensor(path)

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
