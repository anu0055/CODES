import mysql.connector
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Abhianu@125",
    database = "mydatabase"
)
mycursor = mydb.cursor()
sql = "update customers set address = %s WHERE address = %s"
val = ("Canyon 123", "Valley 345")
mycursor.execute(sql, val)
mydb.commit()
print(mycursor.rowcount, "rows affected")