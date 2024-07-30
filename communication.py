import requests
import threading


robot_id = "Logistikroboter" # TODO: Change id to a unique ID for this robot
server_url = 'http://192.168.1.100:5001' # TODO: Change to url of main server

# Send current state to main server
def send_state_async(status):
    json = {"status": status}
    try :
        response = requests.post(f"{server_url}/update_status/{robot_id}", json=json)
        return response.json()
    except :
        return "Unable to update status" 
    

# Send position to main server
def send_position_async(position):
    json = {"position": position}
    try :
        response = requests.post(f"{server_url}/update_position/{robot_id}", json=json)
        return response.json()
    except :
        return "Unable to update position" 
    

# Send path to main server
def send_path_async(path):
    json = {"start": path.start_node, "target": path.target_node}
    try :
        response = requests.post(f"{server_url}/update_path/{robot_id}", json=json)
        return response.json()
    except :
        return "Unable to update path" 
    

# Run function in async as to not interrupt main thread
def run_async(func, *args):
    thread = threading.Thread(target=func, args=args)
    thread.start()


# Send current state to main server
def send_path(path):
    run_async(send_path_async, path)


# Send position to main server
def send_position(position):
    run_async(send_position_async, position)


# Send path to main server
def send_state(status):
    run_async(send_state_async, status)


if __name__ == "__main__":
    print(send_state("started"))