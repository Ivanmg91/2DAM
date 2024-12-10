
mydb = mysql.connector.connect(
    host="edu-dbms",
    user="root",
    password="dbrootpass",
    database="employees",
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM employees")

