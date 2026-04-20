import mysql.connector

database=mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'root',
)

cursor= database.cursor()

cursor.execute('CREATE DATABASE djangoapplications')

print("All done")