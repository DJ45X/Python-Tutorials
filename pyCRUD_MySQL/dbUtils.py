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
            database=database,
            auth_plugin='mysql_native_password'
        )
        return myDb
    except mysql.connector.Error as error:
        print(colored("Error connecting to MySQL:", "red"), colored(error, "magenta"))

# Close Connection
def closeConnection(myDb):
    try:
        myDb.close()
    except mysql.connector.Error as error:
        print(colored("Error closing MySQL connection:", "red"), colored(error, "magenta"))

# Check if Table Exists
def tableExists(tableName):
    try:
        myDb = createConnection()
        cursor = myDb.cursor()

        sql = "SHOW TABLES LIKE %s"
        cursor.execute(sql, (tableName,))
        result = cursor.fetchone()

        if result:
            return True
        else:
            return False

    except mysql.connector.Error as error:
        print(colored("Error checking if table exists:", "red"), colored(error, "magenta"))
    finally:
        cursor.close()
        closeConnection(myDb)

# Check if Column Exists
def columnExists(tableName, columnName):
    try:
        myDb = createConnection()
        cursor = myDb.cursor()

        sql = f"SHOW COLUMNS FROM {tableName} LIKE %s"
        cursor.execute(sql, (columnName,))
        result = cursor.fetchone()

        if result:
            return True
        else:
            return False

    except mysql.connector.Error as error:
        print(colored("Error checking if column exists:", "red"), colored(error, "magenta"))
    finally:
        cursor.close()
        closeConnection(myDb)

# Create Table
def createTable():
    try:
        myDb = createConnection()
        cursor = myDb.cursor()

        sql = "CREATE TABLE customers (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))"
        cursor.execute(sql)

        print(colored("Table created successfully.", "green"))

        cursor.close()
        closeConnection(myDb)
    except mysql.connector.Error as error:
        print(colored("Error creating table:", "red"), colored(error, "magenta"))

# Create Column
def createColumn(tableName, columnName, columnType):
    try:
        myDb = createConnection()
        cursor = myDb.cursor()

        sql = f"ALTER TABLE {tableName} ADD COLUMN {columnName} {columnType}"
        cursor.execute(sql, (tableName, columnName, columnType))

        print(colored("Column created successfully.", "green"))

        cursor.close()
        closeConnection(myDb)
    except mysql.connector.Error as error:
        print(colored("Error creating column:", "red"), colored(error, "magenta"))

# Create Function
def create(name, address):
    try:
        myDb = createConnection()
        cursor = myDb.cursor()

        # Check if table exists, create if it doesn't
        if not tableExists("customers"):
            createTable()

        # Check if name column exists, create if it doesn't
        if not columnExists("customers", "name"):
            createColumn("customers", "name", "VARCHAR(255)")

        # Check if address column exists, create if it doesn't
        if not columnExists("customers", "address"):
            createColumn("customers", "address", "VARCHAR(255)")

        sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
        val = (name, address)
        cursor.execute(sql, val)

        myDb.commit()

        print(colored(cursor.rowcount, "green"), "record inserted.")
        
        cursor.close()
        closeConnection(myDb)
        return "Record inserted successfully"
    except mysql.connector.Error as error:
        print(colored("Error executing create query:", "red"), colored(error, "magenta"))

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
        print(colored("Error executing readAll query:", "red"), colored(error, "magenta"))

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
        print(colored("Error executing searchByName query:", "red"), colored(error, "magenta"))

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
        print(colored("Error executing update query:", "red"), colored(error, "magenta"))

# Delete Function
def delete(name):
    try:
        myDb = createConnection()
        cursor = myDb.cursor()

        sql = "DELETE FROM customers WHERE name = %s"
        val = (name,)
        cursor.execute(sql, val)
        myDb.commit()

        print(colored(f"{cursor.rowcount} record(s) deleted.", "green"))

        cursor.close()
        closeConnection(myDb)
    except mysql.connector.Error as error:
        print(colored("Error executing delete query:", "red"), colored(error, "magenta"))
