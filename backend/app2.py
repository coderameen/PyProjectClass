#passing parament from URL

from flask import Flask,render_template,redirect,request

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>This is ur home page!!</h1>"

@app.route("/user/<name>")
def user(name):
    return f"Hi Welcome {name}"

if __name__=='__main__':
    app.run(debug=True)