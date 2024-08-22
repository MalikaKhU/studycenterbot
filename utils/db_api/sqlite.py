from datetime import datetime
import sqlite3


class Database:
    def __init__(self, path_to_db="main.db"):
        self.path_to_db = path_to_db

    @property
    def connection(self):
        return sqlite3.connect(self.path_to_db)

    def execute(self, sql: str, parameters: tuple = None, fetchone=False, fetchall=False, commit=False):
        if not parameters:
            parameters = ()
        connection = self.connection
        connection.set_trace_callback(logger)
        cursor = connection.cursor()
        data = None
        cursor.execute(sql, parameters)

        if commit:
            connection.commit()
        if fetchall:
            data = cursor.fetchall()
        if fetchone:
            data = cursor.fetchone()
        connection.close()
        return data

   
    @staticmethod
    def format_args(sql, parameters: dict):
        sql += " AND ".join([
            f"{item} = ?" for item in parameters
        ])
        return sql, tuple(parameters.values())


   # -------users table -------------------------------------------
    def insert_user(self, user_id, full_name, username, status, is_left=False):
        sql = "INSERT INTO users (user_id, full_name, username, status, is_left) VALUES(?, ?, ?, ?, ?)"
        self.execute(sql, (user_id, full_name, username, status, is_left), commit=True)

    def select_user(self, user_id):
        sql = "SELECT * FROM users WHERE user_id = ?"
        return self.execute(sql, (user_id,), fetchone=True)
    
    def select_all_users(self):
        sql = "SELECT * FROM users"
        return self.execute(sql, fetchall=True)



def logger(statement):
    print(f"Executing: {statement}")
