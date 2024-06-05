from flask import Flask, request
from threading import Thread
from main import main
from shared import stop_event


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
                main_thread = Thread(target = main) # run main in seperate thread to be able to stop it
                main_thread.start()

                return "started"
            
            return 'already started'
        
        case "stop":
            stop_event.set() # signal the main function to stop

            if main_thread is not None:
                main_thread.join() # wait for the thread to finish
                main_thread = None

            return "stopped"
        
    return 'Aktion konnte nicht ausgeführt werden: ' + command


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
# running on http://raspberrypi.local:5000 or in my case http://192.168.1.32:5000