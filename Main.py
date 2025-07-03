import pickle
import os
from flask import Flask, request

app = Flask(__name__)

@app.route('/process',methods = ['POST'])
def process():
    x1 = float(request.form['x1'])
    x2 = float(request.form['x2'])
    x3 = float(request.form['x3'])
    x4 = float(request.form['x4'])

    x=[[x1,x2,x3,x4]]
    with open('model_iris.pkl','rb') as my_model:
        model = pickle.load(my_model)
    a=model.predict(x)

    return (f"The predicted value is :{a[0]}")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 80))  
    print(f"? Flask server is starting on http://0.0.0.0:{port} ...")
    app.run(host="0.0.0.0", port=port) 

