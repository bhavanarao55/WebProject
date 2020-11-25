import mysql.connector
from FlaskWebProject4 import app
from FlaskWebProject4.DAO.dbConnection import mycursor

def getInterviews():
    mycursor.execute("SELECT * FROM INTERVIEWS")
    return mycursor.fetchall()

def deleteInterviewCandidate(cid):
    mycursor.execute("DELETE FROM INTERVIEWS WHERE candidate_id='"+cid+"';")
    mydb.commit()