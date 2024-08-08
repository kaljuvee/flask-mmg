from flask_security.models import fsqla_v2 as fsqla
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Define models - for this example - we change the default table names
fsqla.FsModels.set_db_info(db, user_table_name="user", role_table_name="role")


class Role(db.Model, fsqla.FsRoleMixin):
    __tablename__ = "role"


class User(db.Model, fsqla.FsUserMixin):
    __tablename__ = "user"


class Hospital(db.Model):
    id = db.Column(db.Integer, primary_key=True)