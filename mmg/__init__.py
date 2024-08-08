from flask import Flask, current_app
from flask_sqlalchemy import SQLAlchemy
from flask_security import (
    Security,
    SQLAlchemyUserDatastore,
    hash_password,
)

# Create database connection object
db = SQLAlchemy()
security = Security()


# Create app
def create_app():
    app = Flask(__name__)

    app.config.from_pyfile('config.py')

    from .user import user_bp
    from .admin import admin_bp
    from .pages import pages_bp
    from .treatments import treatments_bp

    app.register_blueprint(user_bp)
    app.register_blueprint(admin_bp)
    app.register_blueprint(pages_bp)
    app.register_blueprint(treatments_bp)

    from .models import db, User, Role, Hospital

    # Setup Flask-Security
    db.init_app(app)
    user_datastore = SQLAlchemyUserDatastore(db, User, Role)
    security.init_app(app, datastore=user_datastore)

    app.db = db
    app.hospital_cls = Hospital

    return app


# Create users and roles
def create_users():
    if current_app.testing:
        return
    with current_app.app_context():
        security = current_app.security
        security.datastore.db.create_all()
        security.datastore.find_or_create_role(
            name="admin",
            permissions={"admin-read", "admin-write",
                         "user-read", "user-write"},
        )
        security.datastore.find_or_create_role(
            name="user", permissions={"user-read", "user-write"}
        )

        if not security.datastore.find_user(email="admin@me.com"):
            security.datastore.create_user(
                email="admin@me.com",
                password=hash_password("password"),
                roles=["admin"],
            )

        security.datastore.db.session.commit()


if __name__ == "__main__":
    myapp = create_app()
    with myapp.app_context():
        create_users()
    myapp.run()
