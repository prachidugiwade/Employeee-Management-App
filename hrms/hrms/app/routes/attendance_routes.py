from flask import Blueprint, request, jsonify
from app.services.attendance_service import mark_attendance, get_attendance_by_employee

attendance_bp = Blueprint(
    "attendance", __name__, url_prefix="/api/attendance"
)


@attendance_bp.route("", methods=["POST"])
def mark_attendance_api():
    """
    Mark attendance for an employee.
    """
    data = request.get_json()
    mark_attendance(data)
    return jsonify({"message": "Attendance recorded"}), 201


@attendance_bp.route("/<int:employee_id>", methods=["GET"])
def get_attendance(employee_id):
    """
    Get attendance records for an employee.
    """
    records = get_attendance_by_employee(employee_id)
    return jsonify([record.to_dict() for record in records]), 200
