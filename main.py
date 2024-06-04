from navigate import *
import robot
import camera
from loop import loop


def main():
    print("\033[32mStarting...\033[0m\n")

    robot.init()
    camera.init()

    start_point = input_tuple("Enter start point x, y. \nRecommended start points are (1, 6), (1, 5), (1, 3), (1, 2): ")
    direction = input_tuple("Enter robot direction x, y. \nRecommend direction is (0, -1): ")
    print()

    loop(start_point, direction)


def input_tuple(prompt):
    user_input = input(prompt)
    input_parts = user_input.split(",")
    return (int(input_parts[0]), int(input_parts[1]))


if __name__ == "__main__":
    main()