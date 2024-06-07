from gpiozero import InputDevice
from path import Path
from communication import send_state


count_sensor = InputDevice(17)
points = 0
state = False

def check_sensor(path: Path, backwards=False):
    if not path.track_points:
        return

    global points
    global state

    if count_sensor.is_active: # The sensor is active when it is above a point
        if backwards: # If robot is driving backwards, don't count it as a point as the robot has already counted this point
            state = True
        if not state:
            state = True
            points += 1

            print(f"New Point detected. Point {points}/{path.distance_to_target}")

    else:
        state = False

    if points == path.distance_to_target:
        path.finished = True

        print("\n\033[32mArrived at destination!\033[0m")
        send_state("Ziel erreicht!")

        points = 0
        state = False

        return True

    return False
