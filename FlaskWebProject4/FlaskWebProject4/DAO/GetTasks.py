import mysql.connector
from FlaskWebProject4 import app
from FlaskWebProject4.DAO.dbConnection import mycursor, mydb

def getTasks(user_id):
    mycursor.execute("SELECT * FROM TASKS where user_id='"+user_id+"';")
    return mycursor.fetchall()

def deleteTask(tid):
    mycursor.execute("DELETE FROM TASKS WHERE task_id='"+tid+"';")
    mydb.commit()