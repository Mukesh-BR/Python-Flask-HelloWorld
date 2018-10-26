from flask import Flask
import numpy as np
import sklearn
app = Flask(__name__)

@app.route('/')
def hello_world():
  a = np.array([1,2,3])
  return str(a[0])

if __name__ == '__main__':
  app.run()


