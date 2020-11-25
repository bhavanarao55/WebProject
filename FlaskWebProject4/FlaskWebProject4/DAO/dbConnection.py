from flask import Flask
import mysql.connector

mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="bunny55",
        database="PROJECT"
        )
mycursor = mydb.cursor()