from flask import Flask
import socket

app = Flask(__name__)

@app.route("/")
def hello():
  return f"<h1>Hello World!</h1><h3>Flask app is running on {socket.gethostname()}</h3>"

if __name__ == "__main__":
  app.run()
