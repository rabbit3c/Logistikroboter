from navigate import *
import robot
import sensors.camera as camera
from loop import loop
from threading import Thread


def main():
    print("\033[32mStarting...\033[0m\n")

    init()

    # start_point = input_tuple("Enter start point x, y. \nRecommended start points are (1, 6), (1, 5), (1, 3), (1, 2): ")
    start_point = (1, 2)
    # direction = input_tuple("Enter robot direction x, y. \nRecommend direction is (0, -1): ")
    direction = (0, -1)
    print()

    loop(start_point, direction)


def init():
    #initialize camera and robot in seperate threads to decrease startup time
    camera_thread = Thread(target=camera.init)
    robot_thread = Thread(target=robot.init)

    camera_thread.start()
    robot_thread.start()

    camera_thread.join()
    robot_thread.join()


def input_tuple(prompt):
    user_input = input(prompt)
    input_parts = user_input.split(",")
    return (int(input_parts[0]), int(input_parts[1]))


if __name__ == "__main__":
    main()