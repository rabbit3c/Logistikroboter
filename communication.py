import requests
from flask import jsonify


robot_id = "Logistikroboter"
server_url = 'http://192.168.1.100:5001'


def send_state(status):
    json = {"status": status}
    try :
        response = requests.post(f"{server_url}/update/{robot_id}", json=json)
        return response.json()
    except :
        return "Unable to update status" 


if __name__ == "__main__":
    print(send_state("started"))