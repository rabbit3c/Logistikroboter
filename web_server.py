from flask import Flask, request, jsonify
from threading import Thread
from main import run
from shared import stop_event
from communication import send_state
import data.data as data
import robot


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

            if main_thread is None:
                main_thread = Thread(target = run) # run main in seperate thread to be able to stop it
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
        
    return 'Aktion konnte nicht ausgeführt werden: ' + command


@app.route('/set_values', methods = ['POST'])
def set_value():
    start_position = (int(request.form['x_coordinate']), int(request.form['y_coordinate']))
    start_direction = (int(request.form['x_direction']), int(request.form['y_direction']))

    data.get()

    if start_position is not None:
        data.data.start_position = start_position

    if start_direction is not None:
        data.data.start_direction = start_direction

    data.save()

    return 'Saved values'


@app.route('/get_values', methods = ['GET'])
def get_value():
    data.get()

    x_coordinate = data.data.start_position[0]
    y_coordinate = data.data.start_position[1]

    x_direction = data.data.start_direction[0]
    y_direction = data.data.start_direction[1]

    return jsonify({
        "x_coordinate": x_coordinate,
        "y_coordinate": y_coordinate,
        "x_direction": x_direction,
        "y_direction": y_direction
    })


if __name__ == "__main__":
    send_state("stopped")
    app.run(host='0.0.0.0', port=5000)
# running on http://raspberrypi.local:5000 or in my case http://192.168.1.32:5000