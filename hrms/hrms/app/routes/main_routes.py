
from flask import Blueprint, render_template, request, redirect, url_for
from app.services.employee_service import get_all_employees, get_employee_by_id, create_employee
from app.services.attendance_service import get_attendance_by_employee, mark_attendance
from app.services.report_service import get_department_stats

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    """
    Home page route.
    Displays a welcome message and a list of all employees.
    """
    employees = get_all_employees()
    return render_template('index.html', employees=employees)

@main_bp.route('/employee/<int:employee_id>')
def employee_details(employee_id):
    """
    Employee details route.
    Displays detailed information about an employee and their attendance history.
    """
    employee = get_employee_by_id(employee_id)
    attendance_records = get_attendance_by_employee(employee_id)
    return render_template('employee_details.html', employee=employee, attendance_records=attendance_records)

@main_bp.route('/reports')
def reports():
    """
    Reports page route.
    Displays charts and tables for HR reports.
    """
    return render_template('report.html')

@main_bp.route('/add_employee_ui', methods=['GET', 'POST'])
def add_employee_ui():
    """
    UI for adding a new employee.
    """
    if request.method == 'POST':
        data = {
            "name": request.form['name'],
            "email": request.form['email'],
            "address": request.form['address'],
            "designation": request.form['designation'],
            "department": request.form['department'],
            "date_of_joining": request.form['date_of_joining']
        }
        create_employee(data)
        return redirect(url_for('main.index'))
    return render_template('add_employee.html')

@main_bp.route('/mark_attendance_ui', methods=['POST'])
def mark_attendance_ui():
    """
    UI form submission for marking attendance.
    """
    data = {
        "employee_id": request.form['employee_id'],
        "date": request.form['date'],
        "in_time": request.form['in_time'],
        "out_time": request.form['out_time']
    }
    mark_attendance(data)
    return redirect(url_for('main.employee_details', employee_id=request.form['employee_id']))
