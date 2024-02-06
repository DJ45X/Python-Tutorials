import mysql.connector
import os
from dotenv import load_dotenv
from termcolor import colored

# Create Connection
def createConnection():
    # Load Environment Variables
    load_dotenv()
    host = os.getenv("DB_HOST")
    user = os.getenv("DB_USER")
    password = os.getenv("DB_PASSWORD")
    database = os.getenv("DB_DATABASE")

    try:
        myDb = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        return myDb
    except mysql.connector.Error as error:
        print(colored("Error connecting to MySQL:", "red"), error)

# Close Connection
def closeConnection(myDb):
    try:
        myDb.close()
    except mysql.connector.Error as error:
        print(colored("Error closing MySQL connection:", "red"), error)

# Create Function
def create(name, address):
    try:
        myDb = createConnection()
        cursor = myDb.cursor()

        sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
        val = (name, address)
        cursor.execute(sql, val)

        myDb.commit()

        print(colored(cursor.rowcount, "green"), "record inserted.")
        
        cursor.close()
        closeConnection(myDb)
    except mysql.connector.Error as error:
        print(colored("Error executing create query:", error, "red"))

# Read All Function
def readAll():
    try:
        myDb = createConnection()
        cursor = myDb.cursor()

        sql = "SELECT * FROM customers"
        cursor.execute(sql)
        result = cursor.fetchall()

        for x in result:
            print(colored(x, "light_blue"))
        
        cursor.close()
        closeConnection(myDb)
    except mysql.connector.Error as error:
        print(colored("Error executing readAll query:", "red"), error)

# Search By Name Function
def searchByName(name):
    try:
        myDb = createConnection()
        cursor = myDb.cursor()

        sql = "SELECT * FROM customers WHERE name = %s"
        cursor.execute(sql, (name,))
        result = cursor.fetchall()

        for x in result:
            print(colored(x, "light_blue"))
        
        cursor.close()
        closeConnection(myDb)
    except mysql.connector.Error as error:
        print(colored("Error executing searchByName query:", "red"), error)

# Update Function
def update(oldName, newName, newAddress):
    try:
        myDb = createConnection()
        cursor = myDb.cursor()

        sql = "UPDATE customers SET name = %s, address = %s WHERE name = %s"
        val = (newName, newAddress, oldName)
        cursor.execute(sql, val)
        myDb.commit()

        print(colored(cursor.rowcount, "green"), "record(s) affected.")

        cursor.close()
        closeConnection(myDb)
    except mysql.connector.Error as error:
        print(colored("Error executing update query:", "red"), error)

# Delete Function
def delete(name):
    try:
        myDb = createConnection()
        cursor = myDb.cursor()

        sql = "DELETE FROM customers WHERE name = %s"
        val = (name,)
        cursor.execute(sql, val)
        myDb.commit()

        print(colored(cursor.rowcount, "record(s) deleted.", "green"))

        cursor.close()
        closeConnection(myDb)
    except mysql.connector.Error as error:
        print(colored("Error executing delete query:", "red"), error)
