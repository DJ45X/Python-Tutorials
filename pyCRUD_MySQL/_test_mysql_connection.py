import unittest
import mysql.connector
from mysql.connector import Error
from dotenv import load_dotenv
import os
from dbUtils import create, delete

load_dotenv()

class TestMySQLConnection(unittest.TestCase):
    def setUp(self):
        self.host = os.getenv("DB_HOST")
        self.user = os.getenv("DB_USER")
        self.password = os.getenv("DB_PASSWORD")
        self.database = os.getenv("DB_DATABASE")

    def test_connection(self):
        try:
            myDb = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database,
                auth_plugin='mysql_native_password'
            )
            assert myDb.is_connected()
            myDb.close()
        except Error as e:
            print(f"Error: '{e}'")
            self.fail()

class TestCreateFunction(unittest.TestCase):
    def test_create(self):
        try:
            self.name = "Test_Name"
            self.address = "Test_Address"
            result = create(self.name, self.address)
            self.assertEqual(result, "Record inserted successfully")
                
        except Error as e:
            print(f"Error: '{e}'")
            self.fail()

    def tearDown(self):
        delete(self.name)

if __name__ == "__main__":
    unittest.main()