from flask import Flask
from service import service

app = Flask(__name__)

@app.route("/", methods = ["GET"])
def hello():
    return "Hello"

@app.route("/useful_information", methods = ["GET"])
def get_all_information():
    info = service.get_all_information()
    return info

if __name__ == "__main__":
    app.run(debug = True, port = 5000)
