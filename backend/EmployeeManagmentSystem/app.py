from flask import Flask,render_template,request,redirect
from database import conn,cursor

app = Flask(__name__)

@app.route("/")
def home():
    res = cursor.execute('''SELECT * FROM employees''')
    res = res.fetchall()
    return render_template('home.html',res=res)


@app.route("/add")
def add():
    return render_template('add.html')

@app.route("/adddb", methods=['GET','POST'])
def adddb():
    if request.method == 'POST':
        empid = request.form['empid']
        empname = request.form['empname']
        empdesignation = request.form['empdesignation']
        # print([empid,empname,empdesignation])
        
        cursor.execute('''INSERT INTO employees(empid,empname,empdesignation) VALUES(?,?,?)''',(empid,empname,empdesignation))
        conn.commit()
        print("Employee records have been stored successfully")
        
        return redirect("/")
    
@app.route("/edit/<id>")
def edit(id):
    res = cursor.execute('''SELECT * FROM employees WHERE empid=?''',(id,))
    res = res.fetchone()
    return render_template('edit.html',res=res)


@app.route("/editdb", methods=['GET','POST'])
def editdb():
    if request.method == 'POST':
        empid = request.form['empid']
        empname = request.form['empname']
        empdesignation = request.form['empdesignation']
        
        cursor.execute('''UPDATE employees SET empname=?,empdesignation=? WHERE empid=?''',(empname,empdesignation,empid))
        conn.commit()
        return redirect("/")
 
@app.route("/delete/<id>") 
def delete(id):
    cursor.execute('''DELETE FROM employees WHERE empid=?''',(id,)) 
    conn.commit()
    return redirect("/")    
if __name__=='__main__':
    app.run(debug=True)