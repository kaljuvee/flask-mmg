from flask import Blueprint, render_template

pages_bp = Blueprint("pages", __name__)


@pages_bp.route("/")
@pages_bp.route("/home")
def home():
    return render_template("pages/home.html")


@pages_bp.route("/about")
def about():
    return render_template("pages/about.html")
