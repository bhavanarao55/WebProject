import mysql.connector
from FlaskWebProject4 import app
from flask import render_template
from FlaskWebProject4.Utils.RandomGeneration import get_candidate_id
from FlaskWebProject4.DAO.dbConnection import mydb, mycursor

def submitHiringCandidate(Firstname, Lastname, EmailID, Contact_Number, Visa_Status, College_Name1, College_Name2, reference):
    sql = "INSERT INTO CANDIDATES (candidate_id, Firstname, Lastname, EmailID, Contact_Number, Visa_Status, College_Name1, College_Name2, reference, state) VALUES ('" + get_candidate_id() + "','" + Firstname + "','" + Lastname + "','" + EmailID + "','" + Contact_Number + "','" + Visa_Status + "','" + College_Name1 + "','" + College_Name2 + "','" + reference + "','0');"

    try:
        mycursor.execute(sql)
    except mysql.connector.Error as err:
        print('error')
    finally:
        mydb.commit()