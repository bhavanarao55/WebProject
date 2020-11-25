import mysql.connector
from FlaskWebProject4 import app
from FlaskWebProject4.DAO.dbConnection import mycursor,mydb

def getCandidates():
    mycursor.execute("SELECT * FROM CANDIDATES")
    return mycursor.fetchall()

def getMarketingCandidates():
    mycursor.execute("SELECT candidate_id from CANDIDATES where state='1'")
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

def saveHiringCandidate(cid,Firstname,Lastname,EmailID,India_Number,US_Number,Visa_Status,College_Name1,College_Name2,India_Address,US_Address,reference):
    mycursor.execute("UPDATE CANDIDATES SET Firstname='"+ Firstname +"', Lastname='"+ Lastname +"', EmailID='"+ EmailID +"', India_Number='"+ India_Number +"', US_Number='"+ US_Number +"', Visa_Status='"+ Visa_Status +"', College_Name1='"+ College_Name1 +"', College_Name2='"+ College_Name2 +"', India_Address='"+ India_Address +"', US_Address='"+ US_Address +"', reference='"+ reference +"' WHERE candidate_id='" +cid +"';")
    mydb.commit()

def deletePlacedCandidate(cid):
    mycursor.execute("DELETE FROM CANDIDATES WHERE candidate_id='"+cid+"';")
    mydb.commit()