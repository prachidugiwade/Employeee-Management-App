
from app.extensions import db
from app.models.employee import Employee
from datetime import datetime

def create_employee(data):
    """
    Create a new employee record.
    """
    date_of_joining = data.get("date_of_joining")
    if isinstance(date_of_joining, str):
         date_of_joining = datetime.strptime(date_of_joining, "%Y-%m-%d").date()
    
    employee = Employee(
        name=data["name"],
        email=data["email"],
        address=data.get("address"),
        designation=data.get("designation"),
        department=data.get("department"),
        date_of_joining=date_of_joining,
    )

    db.session.add(employee)
    db.session.commit()
    return employee

def get_all_employees():
    """
    Retrieve all employees from database.
    """
    return Employee.query.all()

def get_employee_by_id(employee_id):
    """
    Retrieve employee by ID.
    """
    return Employee.query.get_or_404(employee_id)
