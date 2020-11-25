import mysql.connector
from FlaskWebProject4 import app
from FlaskWebProject4.Utils.RandomGeneration import get_candidate_id
from FlaskWebProject4.DAO.dbConnection import mydb, mycursor

def submitInterviewCandidate(Firstname, Lastname, Consultant_Name, Date, Vendor_Name, Technology, Client_Name, Marketed_by, Interviewer_Names, Feedback, State):
    sql = "INSERT INTO INTERVIEWS (candidate_id, Firstname, Lastname, Consultant_Name, Date, Vendor_Name, Technology, Client_Name, Marketed_By, Interviewer_Names, Feedback, State) VALUES ('" + get_candidate_id() + "','" + Firstname + "','" + Lastname + "','" + Consultant_Name + "','" + Date + "','" + Vendor_Name + "','" + Technology + "','" + Client_Name + "','" + Marketed_by + "','" + Interviewer_Names + "','" + Feedback + "','" + State + "');"
    try:
        mycursor.execute(sql)
    except mysql.connector.Error as err:
        print('error')
    finally:
        mydb.commit()