from gpiozero import InputDevice
from path import Path
from communication import send_state


count_sensor = InputDevice(17)
points = 0
state = True

def check_sensor(path: Path, backwards):
    if not path.track_points:
        return

    global points
    global state

    if count_sensor.is_active: # If sensor changes to true, add a point
        if backwards: # If robot is driving backwards, don't count it as a point
            state = False
        if state:
            state = False
            points += 1
            print(f"New Point detected. Point {points}/{path.distance_to_target}")

    else:
        state = True

    if points == path.distance_to_target:
        path.finished = True
        print("\n\033[32mArrived at destination!\033[32m")
        send_state("Ziel erreicht!")
        points = 0
        return True

    return False