from app.extensions import db


class Attendance(db.Model):
    """
    Attendance database model.
    """

    __tablename__ = "attendance"

    id = db.Column(db.Integer, primary_key=True)
    employee_id = db.Column(
        db.Integer, db.ForeignKey("employees.id"), nullable=False
    )
    date = db.Column(db.Date, nullable=False)
    in_time = db.Column(db.Time)
    out_time = db.Column(db.Time)

    def to_dict(self):
        """Convert attendance object to dictionary."""
        return {
            "id": self.id,
            "employee_id": self.employee_id,
            "date": str(self.date),
            "in_time": str(self.in_time),
            "out_time": str(self.out_time),
        }
