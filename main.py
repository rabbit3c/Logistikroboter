from navigate import *
import robot
import sensors.camera as camera
import data.data as data
from modes import store, deliver
from threading import Thread
from communication import send_state, send_position


# Main function with the ability to chose the operating mode of the robot
def main():
    print("\033[32mChoose option:\033[0m")
    print(" [1]: Store items with robot")
    print(" [2]: Deliver items with robot")
    print(" [3]: Set start values")

    string = input()
    print()

    match string:
        case "1":
            run("store")
        case "2":
            run("deliver")
        case "3":
            set_start_values()
        case _:
            main()


# Run robot in specified mode
def run(mode):
    print("\033[32mStarting...\033[0m\n")
    send_state("Startet...")

    init()

    print()

    send_position(data.data.start_position)

    if mode == "store":
        store(data.data)
    else:
        deliver(data.data)


# Set start position and direction of robot
def set_start_values():
    data.get()
    data.data.start_position = input_tuple("Enter start positions x, y. \nRecommended start positions are (1, 6), (1, 5), (1, 3), (1, 2): ")
    data.data.start_direction = input_tuple("Enter robot direction x, y. \nRecommend direction is (0, -1): ")
    data.save()


# Initialize camera and robot and load data in seperate threads to decrease startup time
def init():
    camera_thread = Thread(target=camera.init)
    robot_thread = Thread(target=robot.init)
    data_thread = Thread(target=data.get)

    camera_thread.start()
    robot_thread.start()
    data_thread.start()

    camera_thread.join()
    robot_thread.join()
    data_thread.join()


# convert input string into tuple
def input_tuple(prompt):
    user_input = input(prompt)
    input_parts = user_input.split(",")
    return (int(input_parts[0]), int(input_parts[1]))


if __name__ == "__main__":
    main()