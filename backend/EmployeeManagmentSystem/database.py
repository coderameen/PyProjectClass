import sqlite3

#Create database and to connect with the database
conn = sqlite3.connect('employeedb.db',check_same_thread=False)
print("Database is created and connected successfully!!")


#cursor: it help to run/execute the query
cursor = conn.cursor()

#To create employee table
cursor.execute('''CREATE TABLE IF NOT EXISTS employees(empid INTEGER PRIMARY KEY,empname TEXT,empdesignation TEXT)''')
print("Employee Table created successfully!")

# #insert data 
# cursor.execute('''INSERT INTO employees(empid,empname,empdesignation) VALUES(?,?,?)''',(102,'Zuhain','Software Tester'))
# conn.commit()
# print("Inserted success!")

