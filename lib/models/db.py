# db.py
import sqlite3

class Database:
    def __init__(self, database_name):
        self.conn = None
        self.cursor = None
        self.database_name = database_name

    def connect(self):
        try:
            self.conn = sqlite3.connect(self.database_name)
            self.cursor = self.conn.cursor()
        except sqlite3.Error as e:
            print("Error connecting to database:", e)

    def close(self):
        if self.conn:
            self.conn.close()

    def commit(self):
        if self.conn:
            self.conn.commit()

    def execute(self, query, params=None):
        try:
            if params:
                self.cursor.execute(query, params)
            else:
                self.cursor.execute(query)
            return self.cursor
        except sqlite3.Error as e:
            print("Error executing query:", e)
            return None

    def create_table(self, table_name, columns):
        columns_str = ", ".join(columns)
        query = f"CREATE TABLE IF NOT EXISTS {table_name} ({columns_str})"
        self.execute(query)
        self.commit()

    def drop_table(self, table_name):
        query = f"DROP TABLE IF EXISTS {table_name}"
        self.execute(query)
        self.commit()
