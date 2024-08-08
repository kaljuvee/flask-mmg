from flask import current_app, Blueprint, render_template, request, redirect, flash

user_bp = Blueprint("user", __name__)


@user_bp.route("/account")
def account():
    return render_template("user/account.html")


@user_bp.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
    return render_template("user/login.html")


@user_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']
        password = request.form['password']
        confirm_password = request.form['confirm_password']

        if password == confirm_password:
            new_user = User(email=email, first_name=first_name,
                            last_name=last_name, password_hash=password)
            db.session.add(new_user)
            flash('Sign Up successful!', 'success')
            return redirect(url_for('user.account'))
        else:
            flash('Passwords do not match.', 'danger')
    return render_template('user/register.html')

