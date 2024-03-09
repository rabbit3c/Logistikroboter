from gpiozero import InputDevice


count_sensor = InputDevice(17)
points = 0
state = True

def check_sensor(path):
    if not path.track_points:
        return

    global points
    global state

    if count_sensor.is_active: # If sensor changes to false, add a point
        if state:
            state = False
            points += 1
            print(f"New Point detected. Point {points}/{path.distance_to_target}")

    else:
        state = True

    if points == path.distance_to_target:
        path.finished = True
        print("Arrived at destination!")

    return points == path.distance_to_target