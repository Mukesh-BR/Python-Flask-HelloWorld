from flask import Flask
import numpy as np
import pickle
app = Flask(__name__)

@app.route('/')
def hello_world():
  return 'Hey its Python Flask application!'

if __name__ == '__main__':
  app.run()







