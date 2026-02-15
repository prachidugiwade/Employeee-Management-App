from flask import Flask
from .config import Config
from .extensions import db, migrate
from .routes.employee_routes import employee_bp
from .routes.attendance_routes import attendance_bp
from .routes.report_routes import report_bp


def create_app():
    """
    Application factory function.
    Initializes Flask app, database, and registers blueprints.
    """
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)

    app.register_blueprint(employee_bp)
    app.register_blueprint(attendance_bp)
    app.register_blueprint(report_bp)
    
    from .routes.main_routes import main_bp
    app.register_blueprint(main_bp)

    return app
