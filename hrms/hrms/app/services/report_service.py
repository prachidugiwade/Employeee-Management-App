
from app.extensions import db
from app.models.employee import Employee
from sqlalchemy import func

def get_department_stats():
    """
    Get count of employees per department.
    """
    result = (
        db.session.query(
            Employee.department,
            func.count(Employee.id)
        )
        .group_by(Employee.department)
        .all()
    )

    return [
        {"department": dept, "count": count}
        for dept, count in result
    ]
