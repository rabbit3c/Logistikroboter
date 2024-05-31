from navigate import *
import a_star
import robot


def main():
    print("Starting...")

    robot.init()
    print()

    # path = a_star.search((2, 8), (10, 2))
    path = a_star.search((11, 7), (8, 2))
    print(path)

    print("Ready!")
    
    while not path.finished:
        navigate(path)


if __name__ == "__main__":
    main()