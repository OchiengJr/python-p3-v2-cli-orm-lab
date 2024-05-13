#!/usr/bin/env python3

from models.department import Department
from models.employee import Employee
import ipdb

def setup_database():
    """Drops existing tables and creates new ones."""
    Employee.drop_table()
    Department.drop_table()
    Department.create_table()
    Employee.create_table()

def seed_data():
    """Populates the database with initial data."""
    # Create departments
    payroll = Department.create("Payroll", "Building A, 5th Floor")
    human_resources = Department.create("Human Resources", "Building C, East Wing")

    # Create employees
    Employee.create("Amir", "Accountant", payroll.id)
    Employee.create("Bola", "Manager", payroll.id)
    Employee.create("Charlie", "Manager", human_resources.id)
    Employee.create("Dani", "Benefits Coordinator", human_resources.id)
    Employee.create("Hao", "New Hires Coordinator", human_resources.id)

def main():
    # Set up database
    setup_database()

    # Seed data
    seed_data()

    # Start debugging session
    ipdb.set_trace()

if __name__ == "__main__":
    main()
