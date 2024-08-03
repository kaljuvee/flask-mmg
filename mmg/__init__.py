from flask import Flask

from mmg import pages
from admin import admin_bp
from pages import bp as pages_bp

def create_app():
    app = Flask(__name__)
    
    app.secret_key = 'supersecretkey'  # Needed for flash messages
    app.register_blueprint(pages_bp)
    app.register_blueprint(admin_bp)
    return app

