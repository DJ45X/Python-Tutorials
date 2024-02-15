import mysql.connector
from mysql.connector import Error
from dotenv import load_dotenv
import os
from dbUtils import create, delete
import pytest

load_dotenv()

class TestMySQLConnection(object):
    def __init__(self):
        self.host = os.getenv("DB_HOST")
        self.user = os.getenv("DB_USER")
        self.password = os.getenv("DB_PASSWORD")
        self.database = os.getenv("DB_DATABASE")
        self.port = os.getenv("DB_PORT")

    def test_connection(self):
        try:
            myDb = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database,
                port=self.port,
                auth_plugin='mysql_native_password'
            )
            assert myDb.is_connected()
            myDb.close()
        except Error as e:
            print(f"Error: '{e}'")
            pytest.fail()

class TestCreateFunction(object):
    def __init__(self):
        self.name = "Test_Name"
        self.address = "Test_Address"

    def test_create(self):
        try:
            result = create(self.name, self.address)
            assert result == "Record inserted successfully"
        except Error as e:
            print(f"Error: '{e}'")
            pytest.fail()

    def __del__(self):
        delete(self.name)

if __name__ == "__main__":
    pytest.main()
