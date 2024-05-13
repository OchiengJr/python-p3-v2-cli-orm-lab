# lib/models/department.py
from db import Database

class Department:
    db = Database("your_database.db")

    # Existing code...

    @classmethod
    def create_table(cls):
        columns = ["id INTEGER PRIMARY KEY", "name TEXT", "location TEXT"]
        cls.db.create_table("departments", columns)

    @classmethod
    def drop_table(cls):
        cls.db.drop_table("departments")

    # Existing code...

# lib/models/employee.py
from db import Database

class Employee:
    db = Database("your_database.db")

    # Existing code...

    @classmethod
    def create_table(cls):
        columns = ["id INTEGER PRIMARY KEY", "name TEXT", "job_title TEXT", "department_id INTEGER"]
        cls.db.create_table("employees", columns)

    @classmethod
    def drop_table(cls):
        cls.db.drop_table("employees")

    # Existing code...
