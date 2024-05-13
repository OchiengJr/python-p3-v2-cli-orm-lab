from models.department import Department
from models.employee import Employee


def exit_program():
    """Exit the program."""
    print("Goodbye!")
    exit()


# Department functions

def list_departments():
    """List all departments."""
    departments = Department.get_all()
    for department in departments:
        print(department)


def find_department_by_name():
    """Find a department by its name."""
    name = input("Enter the department's name: ")
    department = Department.find_by_name(name)
    print(department) if department else print(f'Department {name} not found')


def find_department_by_id():
    """Find a department by its ID."""
    id_ = input("Enter the department's id: ")
    department = Department.find_by_id(id_)
    print(department) if department else print(f'Department {id_} not found')


def create_department():
    """Create a new department."""
    name = input("Enter the department's name: ")
    location = input("Enter the department's location: ")
    try:
        department = Department.create(name, location)
        print(f'Success: {department}')
    except Exception as exc:
        print("Error creating department: ", exc)


def update_department():
    """Update an existing department."""
    id_ = input("Enter the department's id: ")
    if department := Department.find_by_id(id_):
        try:
            name = input("Enter the department's new name: ")
            department.name = name
            location = input("Enter the department's new location: ")
            department.location = location

            department.update()
            print(f'Success: {department}')
        except Exception as exc:
            print("Error updating department: ", exc)
    else:
        print(f'Department {id_} not found')


def delete_department():
    """Delete a department."""
    id_ = input("Enter the department's id: ")
    if department := Department.find_by_id(id_):
        department.delete()
        print(f'Department {id_} deleted')
    else:
        print(f'Department {id_} not found')


# Employee functions (to be implemented)

def list_employees():
    """List all employees."""
    pass


def find_employee_by_name():
    """Find an employee by their name."""
    pass


def find_employee_by_id():
    """Find an employee by their ID."""
    pass


def create_employee():
    """Create a new employee."""
    pass


def update_employee():
    """Update an existing employee."""
    pass


def delete_employee():
    """Delete an employee."""
    pass


def list_department_employees():
    """List all employees in a department."""
    pass
