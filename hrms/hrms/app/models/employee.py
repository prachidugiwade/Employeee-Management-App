from app.extensions import db


class Employee(db.Model):
    """
    Employee database model.
    """

    __tablename__ = "employees"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    address = db.Column(db.String(200))
    designation = db.Column(db.String(100))
    department = db.Column(db.String(100))
    date_of_joining = db.Column(db.Date)

    attendance_records = db.relationship(
        "Attendance", backref="employee", lazy=True
    )

    def to_dict(self):
        """Convert employee object to dictionary."""
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "address": self.address,
            "designation": self.designation,
            "department": self.department,
            "date_of_joining": str(self.date_of_joining),
        }
