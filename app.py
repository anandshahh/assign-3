from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_cloud():
  return 'Hello From Anand Shah ECS Container!'
  
@app.route('/host')
def host_info():
  return 'Hello Anand'


@app.route('/anand')
def aman_info():
  return 'Hello Anand Shah'


app.run(host='0.0.0.0')
