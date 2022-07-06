#Database functions
import mysql.connector

et_db = mysql.connector.connect(
    host = "localhost",
    user = "u",
    password = "y"
)

mycursor = et_db.cursor()
mycursor.execute("Create DB")