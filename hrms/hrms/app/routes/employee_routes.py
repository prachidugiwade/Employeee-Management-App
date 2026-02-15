from flask import Blueprint, request, jsonify
from app.services.employee_service import create_employee, get_all_employees

employee_bp = Blueprint("employees", __name__, url_prefix="/api/employees")


@employee_bp.route("", methods=["POST"])
def add_employee():
    """
    Add a new employee.
    """
    data = request.get_json()
    create_employee(data)
    return jsonify({"message": "Employee created"}), 201


@employee_bp.route("", methods=["GET"])
def get_employees():
    """
    Retrieve all employees.
    """
    employees = get_all_employees()
    return jsonify([emp.to_dict() for emp in employees]), 200
