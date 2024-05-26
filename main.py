from navigate import *
import a_star
import robot


def main():
    print("Starting...")

    robot.init()
    print()

    path = a_star.search((1, 2), (7, 5))
    print(path)

    print("Ready!")
    
    while not path.finished:
        navigate(path)


if __name__ == "__main__":
    main()