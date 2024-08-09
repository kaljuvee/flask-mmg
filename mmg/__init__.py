from flask import Flask
from sqlalchemy import text
from flask_security import (
    Security,
    SQLAlchemyUserDatastore,
    hash_password,
)


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

    app.security = Security(app, datastore=user_datastore)

    app.db = db
    app.hospital_cls = Hospital

    # Create database, roles and base users
    create_database(app)
    create_users(app)

    return app


# Create users and roles
def create_users(myapp):
    with myapp.app_context():
        if myapp.testing:
            return

        security = myapp.security
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

        if not security.datastore.find_user(email="user@me.com"):
            security.datastore.create_user(
                email="user@me.com",
                password=hash_password("password"),
                roles=["user"]
            )

        security.datastore.db.session.commit()


def create_database(myapp):
    with myapp.app_context():
        # Check if the 'users' table exists in the current database
        table_exists = myapp.db.session.execute(
            text(''' SELECT EXISTS
            (SELECT 1 FROM information_schema.tables
            WHERE table_name='user')''')
        ).scalar()

        if table_exists:
            print("Database already exists. Skipping creation.")
        else:
            print(
                "Database or table 'user' does not exist. Creating database.")
            myapp.db.create_all()
