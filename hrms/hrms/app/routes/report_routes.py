from flask import Blueprint, jsonify
from app.services.report_service import get_department_stats

report_bp = Blueprint("reports", __name__, url_prefix="/api/reports")


@report_bp.route("/departments", methods=["GET"])
def department_report():
    """
    Get count of employees per department.
    """
    report = get_department_stats()
    return jsonify(report), 200
