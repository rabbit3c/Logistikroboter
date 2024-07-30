import scanner
import a_star
import robot
import time
import data.data as d
from serial_communication import set_speed
from navigate import navigate
from shared import stop_event, emergency_stop_event
from communication import send_state, send_position, send_path


# First mode: Scanning Barcode, Storing Item at this place and then going back and scanning next barcode
def store(data: d.Data):
    while not stop_event.is_set():
        end_point = scanner.scan()
        
        # Driving to coordinates on barcode to store the item
        path = a_star.search(data.start_position, end_point, data.start_direction)
        navigate_path(path)
        robot.unload(path.direction_target)
        time.sleep(2)

        # Driving back to item pick-up
        path = a_star.search(end_point, data.start_position, path.direction_end, direction_end=data.start_direction)
        navigate_path(path)

    print("Stopping robot...")


# Second mode: Taking first item from List, getting this item and depositing it, then take next item
def deliver(data: d.Data):
    # Driving to first item to pick up
    path = a_star.search(data.start_position, d.items[0], data.start_direction)
    navigate_path(path)

    # Delivering item at item delivery
    path = a_star.search(d.items[0], data.delivery_position, path.direction_end, direction_end=data.delivery_direction)
    navigate_path(path)
    d.items.pop(0)

    for item_position in d.items:
        # Driving to next item to pick up
        path = a_star.search(data.delivery_position, item_position, path.direction_end)
        navigate_path(path)
        time.sleep(3)

        # Delivering next item at item delivery
        path = a_star.search(item_position, data.delivery_position, path.direction_end, direction_end=data.delivery_direction)
        navigate_path(path)
        time.sleep(3)

    # Driving back to start position
    path = a_star.search(data.delivery_position, data.start_position, path.direction_end, direction_end=data.start_direction)
    navigate_path(path)

    print("Stopping robot...")
    send_state("stopped")


# Navigate along given path
def navigate_path(path):
    print(str(path) + "\n")
    send_state(f"Navigiert von {path.start_node} zu {path.target_node}")
    send_position(path.start_node)
    send_path(path)

    print("\033[32mReady!\033[0m\n")
    set_speed(110)
    robot.forward()

    while not path.finished and not emergency_stop_event.is_set():
        navigate(path)

    send_position(path.target_node)
