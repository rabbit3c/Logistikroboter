from navigate import *
from path import Path
import robot

def main():
    print("Starting...")

    robot.init()

    path = Path(3, 6)
    print(path)

    print("Ready!")
    
    while True:
        update_state(path)

if __name__ == "__main__":
    main()