from flask import Flask
import socket

app = Flask(__name__)
hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)

@app.route('/')
def hello_cloud():
  return 'Hello Cloud!'
  
@app.route('/host')
def host_info():
  return 'Hello Form ECS Fargate'


app.run(host='0.0.0.0')
