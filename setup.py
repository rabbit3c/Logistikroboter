from serial_communication import *
from time import time

def right_angle(direction):
    print("Testing length right angle right...")
    print("Press s when the robot has done exactly a right angle")

    start_time = time()
    send_command(f"turn_{direction}")

    stop = input("Press s to stop:")
    if stop == "s":
        duration = time() - start_time
        send_command("stop")
        print(f"The robot took {duration} seconds to turn.")
        sleep(1)


def main():
    print("Setting up robot...")

    communication_test()

    set_speed(100)

    right_angle("right")
    right_angle("left")

    print("Setup complete")



if __name__ == "__main__":
    main()