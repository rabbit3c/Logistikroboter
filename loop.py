import scanner
import a_star
import robot
import time
from serial_communication import set_speed
from navigate import navigate
from shared import stop_event


def loop(start_point, direction):
    while not stop_event.is_set():
        end_point = scanner.scan()
        
        path = a_star.search(start_point, end_point, direction)
        navigate_path(path)

        time.sleep(3)

        path = a_star.search(end_point, start_point, path.direction_end, direction_end=direction)
        navigate_path(path)

    print("Stopping robot...")


def navigate_path(path):
    print(str(path) + "\n")

    print("\033[32mReady!\033[0m\n")
    set_speed(90)
    robot.forward()

    while not path.finished and not stop_event.is_set():
        navigate(path)

