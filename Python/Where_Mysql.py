import mysql.connector 

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Abhianu@125",
    database = "mydatabase"
)

mycursor = mydb.cursor()

sql = "SELECT * FROM customers WHERE address = %s"
adr = ("Park Lane 38", )
mycursor.execute(sql, adr)
myresult = mycursor.fetchall()

for x in myresult:
    print(x)