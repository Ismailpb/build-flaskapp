from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
  return "<h1><center>Hello, World! Flask Application 1</h1></center>"


app.run(host='0.0.0.0', port=7000)
