from os import environ  # Loading secret variables from .env file


def get_env_variable(name):
    try:
        return environ[name]
    except KeyError:
        message = f"Expected environment variable '{name}' not set."
        raise Exception(message)


SQLALCHEMY_DATABASE_URI = get_env_variable("SQLALCHEMY_DATABASE_URI")

SECRET_KEY = get_env_variable("SECRET_KEY")

SECURITY_PASSWORD_SALT = get_env_variable("SECURITY_PASSWORD_SALT")


# Take password complexity seriously
# SECURITY_PASSWORD_COMPLEXITY_CHECKER = "zxcvbn"

DEBUG = True

SECURITY_PASSWORD_HASH = "argon2"
# argon2 uses double hashing by default - so provide key.


# Take password complexity seriously
SECURITY_PASSWORD_COMPLEXITY_CHECKER = "zxcvbn"

# Allow registration of new users without confirmation
SECURITY_REGISTERABLE = True

SQLALCHEMY_TRACK_MODIFICATIONS = False

SQLALCHEMY_TRACK_MODIFICATIONS = False

# As of Flask-SQLAlchemy 2.4.0 it is easy to pass in options directly to the
# underlying engine. This option makes sure that DB connections from the pool
# are still valid. Important for entire application since many DBaaS options
# automatically close idle connections.
SQLALCHEMY_ENGINE_OPTIONS = {"pool_pre_ping": True}