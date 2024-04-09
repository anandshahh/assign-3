from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_cloud():
  return 'Hello From Aman's ECS Container!'
  
@app.route('/host')
def host_info():
  return 'Hello Aman'


@app.route('/aman')
def aman_info():
  return 'Hello pipeline is working'


app.run(host='0.0.0.0')
