import mysql.connector
from FlaskWebProject4 import app
from FlaskWebProject4.DAO.dbConnection import mycursor,mydb

def getCandidates():
    mycursor.execute("SELECT * FROM CANDIDATES")
    return mycursor.fetchall()

def getMarketingCandidates():
    mycursor.execute("SELECT candidate_id from CANDIDATES where state='0'")
    return mycursor.fetchcall()

def getHiringCandidates():
    mycursor.execute("SELECT * FROM CANDIDATES where state='0'")
    return mycursor.fetchall()

def getPlacedCandidates():
    mycursor.execute("SELECT * FROM CANDIDATES where state='4'")
    return mycursor.fetchall()

def deleteHiringCandidate(cid):
    mycursor.execute("DELETE FROM CANDIDATES WHERE candidate_id='"+cid+"';")
    mydb.commit()

def updateHiringCandidate(cid):
    mycursor.execute("UPDATE F")
    mydb.commit()