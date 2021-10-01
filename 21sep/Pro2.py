import mysql.connector as mysql

# Mysql Server Connection .... 
conn = mysql.connect(host="localhost",user="root",password="root",database="pydb")

# Cursor Object : for executing SQL queries
cr = conn.cursor()

# Execute Query
cr.execute("select * from student")

while True:
    data = cr.fetchone()
    if data is None:
        break
    print(data)
