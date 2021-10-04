import unittest
import sqlite3
import os


class TestConnection(unittest.TestCase):
    def test_database_readable(self):
        self.assertTrue(os.access("employee.db", os.R_OK))

    def test_create_database(self):
        conn = sqlite3.connect("employee.db")
        cursor = conn.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS STUD_REGISTRATION (STU_ID text, STU_NAME text, STU_EMAIL text,STU_DOB text,STU_GENDER text, STU_CONTACT int, STU_ADDRESS text)")
        conn.commit()
        conn.close()

    def test_update_database(self):
        conn = sqlite3.connect("employee.db")
        cursor = conn.cursor()
        cursor.execute(
            f'UPDATE STUD_REGISTRATION SET STU_ID=1 WHERE STU_ID = ?', [0])
        conn.commit()
        conn.close()

    def test_connect_database(self):
        conn = sqlite3.connect("employee.db")
        conn.close()
