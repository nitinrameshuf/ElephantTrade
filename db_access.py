#Database functions
import mysql

et_db = mysql.connector.connect(
    host = "localhost",
    user = "u",
    password = "y"
)

mycursor = et_db.cursor()
mycursor.execute("Create DB")