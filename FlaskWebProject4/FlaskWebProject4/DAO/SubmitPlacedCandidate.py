import mysql.connector
from FlaskWebProject4 import app
from FlaskWebProject4.Utils.RandomGeneration import get_candidate_id
from FlaskWebProject4.DAO.dbConnection import mydb, mycursor

def submitPlacedCandidate(Firstname, Lastname, EmailID, India_Number, US_Number, Visa_Status, College_Name1, College_Name2, Technology, StartDate, EndDate, Vendor_Name, Client_Name, Job_Location, dollarRate_per_hour, India_Address, US_Address, reference):
    sql = "INSERT INTO CANDIDATES (candidate_id, Firstname, Lastname, EmailID, India_Number, US_Number, Visa_Status, College_Name1, College_Name2, Technology, StartDate, EndDate, Vendor_Name, Client_Name, Job_Location, dollarRate_per_hour,  India_Address, US_Address, reference, state) VALUES ('" + get_candidate_id() + "','" + Firstname + "','" + Lastname + "','" + EmailID + "','" + India_Number + "','" + US_Number + "','" + Visa_Status + "','" + College_Name1 + "','" + College_Name2 + "','" + Technology + "','" + StartDate + "','" + EndDate + "','" + Vendor_Name + "','" + Client_Name + "','" + Job_Location + "','" + dollarRate_per_hour + "','" + India_Address + "','" + US_Address + "','" + reference + ",'4');"
    print("before insert",sql)
    try:
        mycursor.execute(sql)
    except mysql.connector.Error as err:
        print(err)
    finally:
        mydb.commit()