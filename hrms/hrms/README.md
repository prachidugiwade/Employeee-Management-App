
# Basic HRMS (Human Resource Management System)

This project is a Basic HRMS (Human Resource Management System) built with Flask. It simulates employee management, attendance tracking, and basic reporting.

## Features

*   **Employee Management**:
    *   Add new employees with details (Name, Email, Designation, Department, Address, DOJ).
    *   View a list of all employees.
    *   View detailed profile for each employee.
*   **Attendance Tracking**:
    *   Mark attendance (Date, In Time, Out Time) for employees.
    *   View attendance history for each employee.
*   **Reporting**:
    *   Visual report (Bar Chart) showing the count of employees in each department.
    *   Tabular data for department counts.

## Project Structure

```
hrms/
├── app/
│   ├── models/         # Database models (Employee, Attendance)
│   ├── routes/         # API routes and UI views
│   ├── services/       # Business logic layer
│   ├── static/         # CSS and JavaScript files
│   ├── templates/      # HTML templates
│   ├── __init__.py     # App initialization
│   ├── config.py       # Configuration settings
│   └── extensions.py   # Flask extensions (db, migrate)
├── migrations/         # Database migrations
├── app.py              # Entry point
├── config.py           # Configuration
├── requirements.txt    # Python dependencies
└── README.md           # Project documentation
```

## Setup & Installation

1.  **Clone the repository** (if applicable) or extract the zip file.

2.  **Create a Virtual Environment**:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3.  **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4.  **Database Setup**:
    Initialize the database and apply migrations:
    ```bash
    flask db upgrade
    ```
    *Note: If you encounter issues, delete the `hrms.db` file and `migrations` folder, then run `flask db init`, `flask db migrate`, and `flask db upgrade`.*

5.  **Run the Application**:
    ```bash
    python run.py
    ```

6.  **Access the App**:
    Open your web browser and go to `http://127.0.0.1:5000/`.

## API Endpoints

*   `GET /api/employees`: List all employees.
*   `POST /api/employees`: Add a new employee.
*   `POST /api/attendance`: Mark attendance.
*   `GET /api/attendance/<id>`: Get attendance for an employee.
*   `GET /api/reports/departments`: Get department-wise employee count.

## Technologies Used

*   **Backend**: Python, Flask, Flask-SQLAlchemy, Flask-Migrate
*   **Frontend**: HTML5, CSS3, Bootstrap 5, Chart.js, Jinja2 Templates
*   **Database**: SQLite (default)

## Time and Space Complexity Analysis (Bonus)

### 1. Employee Management
*   **Add Employee (`POST /api/employees`)**:
    *   **Time Complexity**: O(1) - Adding a single record to the database takes constant time on average (ignoring index updates).
    *   **Space Complexity**: O(1) - Uses a fixed amount of memory for the employee object.
*   **List Employees (`GET /api/employees`)**:
    *   **Time Complexity**: O(N) - Where N is the number of employees. Retrieving all records requires iterating over the entire table.
    *   **Space Complexity**: O(N) - To store the list of employees in memory before returning the response.

### 2. Attendance Tracking
*   **Mark Attendance (`POST /api/attendance`)**:
    *   **Time Complexity**: O(1) - Inserting a single attendance record takes constant time.
    *   **Space Complexity**: O(1) - Constant space for the attendance object.
*   **Get Attendance (`GET /api/attendance/<id>`)**:
    *   **Time Complexity**: O(M) - Where M is the number of attendance records for a specific employee. With an index on `employee_id`, finding records is efficient, but we still fetch M records.
    *   **Space Complexity**: O(M) - To store the list of attendance records in the response.

### 3. Reporting
*   **Department Report (`GET /api/reports/departments`)**:
    *   **Time Complexity**: O(N) - The database must scan the `employees` table (or an index on `department`) to count employees per department.
    *   **Space Complexity**: O(D) - Where D is the number of unique departments. The result set size depends on the number of departments.

## Author
[Your Name]
