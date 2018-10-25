import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.externals import joblib
from flask import Flask,request
app=Flask(__name__)

@app.route('/')

def main():
	return "Hello World!!Please Work"
	a = int(request.headers.get('A'))
	b = int(request.headers.get('B'))
	c = int(request.headers.get('C'))
	d = int(request.headers.get('D'))

	x_test = np.array([a,b,c,d]).reshape(1,4)

	clf_ne = joblib.load('model_ne.pkl') 
	clf_se = joblib.load('model_se.pkl') 
	clf_sw = joblib.load('model_sw.pkl') 
	clf_nw = joblib.load('model_nw.pkl') 

	ypred_ne=str(abs(clf_ne.predict(x_test)[0]))
	ypred_se=str(abs(clf_se.predict(x_test)[0]))
	ypred_sw=str(abs(clf_sw.predict(x_test)[0]))
	ypred_nw=str(abs(clf_nw.predict(x_test)[0]))
	
	
	#return str(ypred_ne) + " " + str(ypred_se) + " " + str(ypred_sw) + " " + str(ypred_nw) 

if __name__=='__main__':
	app.run()



