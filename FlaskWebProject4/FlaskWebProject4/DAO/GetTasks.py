import mysql.connector
from FlaskWebProject4 import app
from FlaskWebProject4.DAO.dbConnection import mycursor

def getTasks(user_id):
    mycursor.execute("SELECT * FROM TASKS where user_id='"+user_id+"';")
    return mycursor.fetchall()