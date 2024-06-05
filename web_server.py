from flask import Flask, request
from main import main


app = Flask(__name__)


@app.route("/")
def home():
    return "<p>Logistikroboter Web Server<p>"

     
@app.route('/control', methods = ['POST'])
def control():
    action = request.form['action']

    if action == "start":
        main()

    return 'Aktion erhalten: ' + action


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

# running on http://raspberrypi.local:5000 or in my case http://192.168.1.32:5000