import mysql.connector
from FlaskWebProject4 import app
from FlaskWebProject4.DAO.dbConnection import mycursor

def getRandomId(str,id):
    print("SELECT " + str + "_id from " + str + "s where " + str + "_id='" + id + "';")
    mycursor.execute("SELECT " + str + "_id from " + str + "s where " + str + "_id='" + id + "';")
    return mycursor.fetchall()

