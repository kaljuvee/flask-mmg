from flask import Flask
from mmg import pages, user, treatments, admin

def create_app():
    app = Flask(__name__)
    
    app.secret_key = 'supersecretkey'  # Needed for flash messages
    app.register_blueprint(pages.bp)
    app.register_blueprint(user.bp)
    app.register_blueprint(treatments.bp)
    app.register_blueprint(admin.admin_bp)

    return app

