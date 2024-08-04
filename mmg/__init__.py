from flask import Flask
from admin import admin_bp
from mmg import pages, user, treatments

def create_app():
    app = Flask(__name__)
    
    app.secret_key = 'supersecretkey'  # Needed for flash messages
    app.register_blueprint(pages.bp)
    app.register_blueprint(user.bp)
    app.register_blueprint(treatments.bp)
    app.register_blueprint(admin_bp)

    return app

