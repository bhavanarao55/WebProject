import mysql.connector
from FlaskWebProject4 import app
from FlaskWebProject4.DAO.dbConnection import mycursor

def getUsers():
    mycursor.execute("SELECT * FROM USERS")
    return mycursor.fetchall()