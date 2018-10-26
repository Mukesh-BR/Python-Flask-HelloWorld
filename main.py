from flask import Flask,request
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.externals import joblib
app=Flask(__name__)

@app.route('/')

def main():
	# a = request.headers.get('A')
	# b = request.headers.get('B')
	# c = request.headers.get('C')
	# d = request.headers.get('D')

	a=33
	b=77
	c=983
	d=70
	x_test = np.array([a,b,c,d]).reshape(1,4)

	clf_ne = joblib.load('model_ne.pkl') 
	clf_se = joblib.load('model_se.pkl') 
	clf_sw = joblib.load('model_sw.pkl') 
	clf_nw = joblib.load('model_nw.pkl') 

	ypred_ne=str(abs(clf_ne.predict(x_test)[0]))	
	ypred_se=str(abs(clf_se.predict(x_test)[0]))
	ypred_sw=str(abs(clf_sw.predict(x_test)[0]))
	ypred_nw=str(abs(clf_nw.predict(x_test)[0]))
	
	print("Hello World")
	print(request.headers)
	a=request.headers.get('A')
	print(type(a))
	return ypred_ne+" "+ypred_se+" "+ypred_sw+" "+ypred_nw 

if __name__=='__main__':
	app.run(host='192.168.43.48',port=8000)






