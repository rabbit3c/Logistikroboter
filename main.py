from navigate import *
import a_star
import robot
import scanner


def main():
    print("\033[32mStarting...\033[0m\n")

    robot.init()

    start_point = input_tuple("Enter start point x, y: ")
    direction = input_tuple("Enter robot direction x, y: ")
    print()

    end_point = scanner.scan()

    path = a_star.search(start_point, end_point, direction)

    print(str(path) + "\n")

    print("\033[32mReady!\033[0m\n")
    robot.forward()

    while not path.finished:
        navigate(path)


def input_tuple(prompt):
    user_input = input(prompt)
    input_parts = user_input.split(",")
    return (int(input_parts[0]), int(input_parts[1]))


if __name__ == "__main__":
    main()