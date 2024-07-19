from flask import Flask,render_template,request,redirect
import pickle
from database import conn,cursor

#initialize the app
app = Flask(__name__)

model = pickle.load(open('model.pkl','rb'))



@app.route("/")
@app.route("/login")
def login():
    return render_template('loginPage.html')

@app.route("/register")
def register():
    return render_template("registerPage.html")

@app.route("/registerdb", methods=['GET','POST'])
def registerdb():
    if request.method == 'POST':
        username = request.form['usernameinp']
        password = request.form['passwordinp']
        print([username,password])
        #to store values in db
        cursor.execute('''INSERT INTO register(username,password) VALUES(?,?)''',(username,password))
        conn.commit()
        print("data saved in register table!!")
        
        return render_template("index.html")
    


@app.route("/logindb", methods=['GET','POST'])
def logindb():
    if request.method == 'POST':
        username = request.form['usernameinp']
        password = request.form['passwordinp']
        
        # print([username,password])
        res = cursor.execute('''SELECT password FROM register WHERE username=?''',(username,))
        res = res.fetchone()
        # print("====> from db: ",res[0])
        
        if res[0] == password:
            return render_template("index.html", vaidname = username)
        else:
            return render_template("loginresult.html", msg = "Invalid username or password")

#GET API
@app.route("/index")
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
    app.run(debug=True, port=5001)