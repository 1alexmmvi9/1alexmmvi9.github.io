import mysql.connector

connector = mysql.connector.connect(
        host='localhost',
        user='avisolegal',
        password='avisolegal',
        database='avisolegal',
    )

cursor = connector.cursor() 
