
from app.extensions import db
from app.models.attendance import Attendance
from datetime import datetime

def mark_attendance(data):
    """
    Mark attendance for an employee.
    """
    
    date = data.get("date")
    in_time = data.get("in_time")
    out_time = data.get("out_time")
    
    if isinstance(date, str):
        date = datetime.strptime(date, "%Y-%m-%d").date()
    if isinstance(in_time, str):
        in_time = datetime.strptime(in_time, "%H:%M").time()
    if isinstance(out_time, str):
        out_time = datetime.strptime(out_time, "%H:%M").time()

    attendance = Attendance(
        employee_id=data["employee_id"],
        date=date,
        in_time=in_time,
        out_time=out_time,
    )

    db.session.add(attendance)
    db.session.commit()
    return attendance

def get_attendance_by_employee(employee_id):
    """
    Get attendance records for an employee.
    """
    return Attendance.query.filter_by(employee_id=employee_id).all()
