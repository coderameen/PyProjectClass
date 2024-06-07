#Backend in python: Flask Framework
#Flask: it is a backend framework used to develop software application
#to installl flask: In cmd: "pip install flask"


#import flask
from flask import Flask,render_template,redirect,request

#to initialize the flask app
app = Flask(__name__)

#default Route , @=>Decorator
@app.route("/")
def home():
    return "Hello guys welcome to flask backend in python"

@app.route("/service")
def service():
    return "This is service page!!"


@app.route("/contact")
def contact():
    return "this is my contace page!!"

@app.route("/login")
def login():
    return "This is login page"

@app.route("/logout")
def logout():
    return redirect("/")
        
if __name__=='__main__':
    app.run(debug=True)