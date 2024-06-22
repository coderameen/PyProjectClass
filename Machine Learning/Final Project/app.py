from flask import Flask,render_template,request,redirect
import pickle

#initialize the app
app = Flask(__name__)

model = pickle.load(open('model.pkl','rb'))


#GET API
@app.route("/")
def home():
    return render_template('index.html')

#GET API
@app.route("/predictpage")
def predictpage():
    return render_template('predict.html')


#POST API
@app.route("/predict", methods=['GET','POST'])
def predict():
    if request.method == 'POST':
        #independent parameters
        bp = request.form['bpinp']
        oxy = request.form['oxyinp']
        hb = request.form['hbinp']
        ecg = request.form['ecginp']
        temp = request.form['tempinp']
        
        # print([bp,oxy,hb,ecg,temp])
        pred = model.predict([[bp,oxy,hb,ecg,temp]])
        # print(pred[0])
        
        if pred[0] == 1:
            msg = "Patient Health is Normal"
        elif pred[0] == 2:
            msg = "Patient Health is Mild"
        elif pred[0] == 3:
            msg = "Patient Health is Moderate"
        else:
            msg = "Patient Health is Severe"
        
        return render_template('index.html', msg=msg)
        
if __name__=='__main__':
    app.run(debug=True)