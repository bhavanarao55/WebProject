import mysql.connector
from FlaskWebProject4 import app
from flask import render_template
from FlaskWebProject4.Utils.RandomGeneration import get_task_id
from FlaskWebProject4.DAO.dbConnection import mydb, mycursor

def submitEntry(name, task, details, technology, source, link, time, notes):
    sql = "INSERT INTO TASKS (task_id, name, task, details, technology, source, link, time, notes)" \
          "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
    args = (get_task_id(), name, task, details, technology, source, link, time, notes)
    try:
        mycursor.execute(sql, args)
    except mysql.connector.Error as err:
        print('error')
    finally:
        mydb.commit()