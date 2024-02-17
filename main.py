from line_sensor import *
from serial_communication import*

def main():
    print("Starting...")

    communication_test()

    set_speed(200)

    print("Ready!")
    while True:
        update_state()

if __name__ == "__main__":
    main()