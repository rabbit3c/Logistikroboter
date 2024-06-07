from flask import Flask, request, jsonify
from threading import Thread
from main import run
from shared import stop_event, emergency_stop_event
from communication import send_state
import data.data as data
import robot
import json


app = Flask(__name__)


main_thread = None


@app.route("/")
def home():
    return "<p>Logistikroboter Web Server<p>"
     

@app.route('/control', methods = ['POST'])
def control():
    global main_thread

    command = request.form['command']
    match command:
        case "start":
            stop_event.clear()
            emergency_stop_event.clear()
            
            mode = request.form['mode']

            if mode == "deliver":
                data.items = json.loads(request.form['items'])

            if main_thread is None:
                main_thread = Thread(target = run, args=[mode]) # run main in seperate thread to be able to stop it
                main_thread.start()

                return "started"
            
            return 'already started'
        
        case "stop":
            stop_event.set() # signal the main function to stop

            if main_thread is not None:
                main_thread.join() # wait for the thread to finish
                main_thread = None

            robot.stop() # ensure that the robot is stopped

            return "stopped"
        
        case "emergency_stop":
            emergency_stop_event.set() # signal the main function to stop
            stop_event.set()

            if main_thread is not None:
                main_thread.join() # wait for the thread to finish
                main_thread = None

            robot.stop() # ensure that the robot is stopped

            return "emergency_stopped"
        
    return 'Aktion konnte nicht ausgeführt werden: ' + command


@app.route('/set_values', methods = ['POST'])
def set_value():
    start_position = data.array_to_tuple(json.loads(request.form['start_position']))
    start_direction = data.array_to_tuple(json.loads(request.form['start_direction']))
    delivery_position = data.array_to_tuple(json.loads(request.form['delivery_position']))
    delivery_direction = data.array_to_tuple(json.loads(request.form['delivery_direction']))

    data.get()

    if start_position is not None:
        data.data.start_position = start_position

    if start_direction is not None:
        data.data.start_direction = start_direction

    if delivery_position is not None:
        data.data.delivery_position = delivery_position

    if delivery_direction is not None:
        data.data.delivery_direction = delivery_direction

    data.save()

    return 'Saved values'


@app.route('/get_values', methods = ['GET'])
def get_value():
    data.get()

    return jsonify({
        "start_position": data.data.start_position,
        "start_direction": data.data.start_direction,
        "delivery_position": data.data.delivery_position,
        "delivery_direction": data.data.delivery_direction,
    })


if __name__ == "__main__":
    send_state("stopped")
    app.run(host='0.0.0.0', port=5000)
# running on http://raspberrypi.local:5000 or in my case http://192.168.1.32:5000