import requests
import threading


robot_id = "Logistikroboter" # TODO: Change id to a unique ID for this robot
server_url = 'http://192.168.1.100:5001' # TODO: Change to url of main server


def send_state_async(status):
    json = {"status": status}
    try :
        response = requests.post(f"{server_url}/update_status/{robot_id}", json=json)
        return response.json()
    except :
        return "Unable to update status" 
    

def send_position_async(position):
    json = {"position": position}
    try :
        response = requests.post(f"{server_url}/update_position/{robot_id}", json=json)
        return response.json()
    except :
        return "Unable to update position" 
    

def send_path_async(path):
    json = {"start": path.start, "target": path.target}
    try :
        response = requests.post(f"{server_url}/update_path/{robot_id}", json=json)
        return response.json()
    except :
        return "Unable to update path" 
    

def run_async(func, *args):
    thread = threading.Thread(target=func, args=args)
    thread.start()


def send_path(path):
    run_async(send_path_async, path)


def send_position(position):
    run_async(send_position_async, position)


def send_state(status):
    run_async(send_state_async, status)


if __name__ == "__main__":
    print(send_state("started"))