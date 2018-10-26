from flask import Flask
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.externals import joblib
app = Flask(__name__)

@app.route('/')
def hello_world():
  return 'Hey its Python Flask application!'

if __name__ == '__main__':
  app.run()







