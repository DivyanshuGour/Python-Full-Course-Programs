import mysql.connector as mysql

# Mysql Server Connection .... 
conn = mysql.connect(host="localhost",user="root",password="root",database="pydb")

# Cursor Object : for executing SQL queries
cr = conn.cursor()

# Execute Query
cr.execute("insert into student value(105,'Rajesh',21,'dewas',231.11)")

conn.commit()
print("Done !")

conn.close()





