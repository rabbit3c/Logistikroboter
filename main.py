from navigate import *
import robot
import sensors.camera as camera
import data.data as data
from loop import loop
from threading import Thread
from communication import send_state


def main():
    print("\033[32mChoose option:\033[0m")
    print(" [1]: Run robot")
    print(" [2]: Set start values")

    string = input()
    print()

    match string:
        case "1":
            run()
        case "2":
            set_start_values()
        case _:
            main()


def run():
    print("\033[32mStarting...\033[0m\n")
    send_state("Startet...")

    init()

    print()

    loop(data.data.start_position, data.data.start_direction)


def set_start_values():
    data.get()
    data.data.start_position = input_tuple("Enter start positions x, y. \nRecommended start positions are (1, 6), (1, 5), (1, 3), (1, 2): ")
    data.data.start_direction = input_tuple("Enter robot direction x, y. \nRecommend direction is (0, -1): ")
    data.save()


def init():
    #initialize camera and robot and load data in seperate threads to decrease startup time
    camera_thread = Thread(target=camera.init)
    robot_thread = Thread(target=robot.init)
    data_thread = Thread(target=data.get)

    camera_thread.start()
    robot_thread.start()
    data_thread.start()

    camera_thread.join()
    robot_thread.join()
    data_thread.join()


def input_tuple(prompt):
    user_input = input(prompt)
    input_parts = user_input.split(",")
    return (int(input_parts[0]), int(input_parts[1]))


if __name__ == "__main__":
    main()