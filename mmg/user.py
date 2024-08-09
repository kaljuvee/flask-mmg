from flask import current_app, Blueprint, render_template, request, redirect, flash

user_bp = Blueprint("user", __name__)


@user_bp.route("/account")
def account():
    return render_template("user/account.html")



