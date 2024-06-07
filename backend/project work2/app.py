#sending data from backend to frontend using Prototype

from flask import Flask,render_template,redirect,request


app = Flask(__name__)

@app.route('/')
def home():
    res = "This is my message!! fetched data from datable"
    return render_template('home.html', res=res)



@app.route("/service")
def service():
    fruit = ['mange','banana','orange','grapes']
    return render_template('service.html',fruit=fruit)
if __name__=='__main__':
    app.run(debug=True)