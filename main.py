from flask import Flask
import numpy
app = Flask(__name__)

@app.route('/')
def hello_world():
  #a = np.array([1,2,3])
  return "Hello World"

if __name__ == '__main__':
  app.run()


