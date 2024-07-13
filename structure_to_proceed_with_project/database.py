import sqlite3

#creating database and connecting to it
conn = sqlite3.connect('registrationdb.db',  check_same_thread=False)
print("Database created and connected successfully!")


#cursor: help to execute the query

cursor = conn.cursor()
#create the table
cursor.execute('''CREATE TABLE IF NOT EXISTS register(username TEXT PRIMARY KEY, password TEXT)''')
print("Register table created success!")


#insert dummy values/users
# cursor.execute('''INSERT INTO register(username,password) VALUES(?,?)''',("yaseen","yaseen@123"))
# cursor.execute('''INSERT INTO register(username,password) VALUES(?,?)''',("sarita","sarita@123"))
# conn.commit()
# print("created success!")


# cursor.execute('''DROP TABLE resister''')
# print("table dropped!!")
