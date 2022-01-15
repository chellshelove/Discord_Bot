from flask import Flask # use flask as the web server 
from threading import Thread

app = Flask('')

@app.route('/')
def home():
    return "Hello. I am alive!" # return "hello i'm alive" to amyone who visits the server 

def run():
  app.run(host='0.0.0.0',port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start() 