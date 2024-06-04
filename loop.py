import scanner
import a_star
import robot
import time
from navigate import navigate


def loop(start_point, direction):
    while True:
        end_point = scanner.scan()
        
        path = a_star.search(start_point, end_point, direction)
        navigate_path(path)

        time.sleep(3)

        path = a_star.search(end_point, start_point, path.direction_end, direction_end=direction)
        navigate_path(path)


def navigate_path(path):
    print(str(path) + "\n")

    print("\033[32mReady!\033[0m\n")
    robot.forward()

    while not path.finished:
        navigate(path)

