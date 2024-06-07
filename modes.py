import scanner
import a_star
import robot
import time
import data.data as d
from serial_communication import set_speed
from navigate import navigate
from shared import stop_event, emergency_stop_event
from communication import send_state, send_position, send_path


def store(data: d.Data):
    while not stop_event.is_set():
        end_point = scanner.scan()
        
        path = a_star.search(data.start_position, end_point, data.start_direction)
        navigate_path(path)

        path = a_star.search(end_point, data.start_position, path.direction_end, direction_end=data.start_direction)
        navigate_path(path)

    print("Stopping robot...")


def deliver(data: d.Data):
    path = a_star.search(data.start_position, d.items[0], data.start_direction)
    navigate_path(path)

    path = a_star.search(d.items[0], data.delivery_position, path.direction_end, direction_end=data.delivery_direction)
    navigate_path(path)
    d.items.pop(0)

    for item_position in d.items:
        path = a_star.search(data.delivery_position, item_position, path.direction_end)
        navigate_path(path)

        path = a_star.search(item_position, data.delivery_position, path.direction_end, direction_end=data.delivery_direction)
        navigate_path(path)

    path = a_star.search(data.delivery_position, data.start_position, path.direction_end, direction_end=data.start_direction)
    navigate_path(path)

    print("Stopping robot...")
    send_state("stopped")


def navigate_path(path):
    print(str(path) + "\n")
    send_state(f"Navigiert von {path.start} zu {path.target}")
    send_position(path.start)
    send_path(path)

    print("\033[32mReady!\033[0m\n")
    set_speed(110)
    robot.forward()

    while not path.finished and not emergency_stop_event.is_set():
        navigate(path)

    send_position(path.target)

    time.sleep(3)
