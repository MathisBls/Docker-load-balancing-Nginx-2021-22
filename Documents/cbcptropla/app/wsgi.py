from flask import Flask
import socket

app = Flask(__name__)

@app.route('/')

def index():
    return 'Hello World ! ID des containers: ' + str(socket.gethostname())

if __name__ == '__main__':
    app.run(debug=True)