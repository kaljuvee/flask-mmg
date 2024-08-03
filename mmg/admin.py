from flask import Blueprint, render_template, request, redirect, url_for, flash
import pandas as pd

admin_bp = Blueprint("admin", __name__, url_prefix='/admin')

# Function to load user data from a CSV file (you can use a database instead)
def load_user_data():
    try:
        return pd.read_csv('user_data.csv')
    except FileNotFoundError:
        return pd.DataFrame(columns=['user_id', 'email', 'password_hash', 'first_name', 'last_name', 'phone_number'])

# Function to save user data to a CSV file (you can use a database instead)
def save_user_data(user_data_df):
    user_data_df.to_csv('user_data.csv', index=False)

@admin_bp.route("/users")
def list_users():
    user_data = load_user_data()
    return render_template("admin/list_users.html", users=user_data.to_dict(orient='records'))

@admin_bp.route("/users/new", methods=['GET', 'POST'])
def new_user():
    if request.method == 'POST':
        user_data = load_user_data()
        new_user = {
            'user_id': len(user_data) + 1,
            'email': request.form['email'],
            'password_hash': request.form['password'],
            'first_name': request.form['first_name'],
            'last_name': request.form['last_name'],
            'phone_number': request.form['phone_number']
        }
        user_data = user_data.append(new_user, ignore_index=True)
        save_user_data(user_data)
        flash('User created successfully!', 'success')
        return redirect(url_for('admin.list_users'))
    return render_template("admin/new_user.html")

@admin_bp.route("/users/edit/<int:user_id>", methods=['GET', 'POST'])
def edit_user(user_id):
    user_data = load_user_data()
    user = user_data.loc[user_data['user_id'] == user_id].to_dict(orient='records')[0]
    if request.method == 'POST':
        user_data.loc[user_data['user_id'] == user_id, ['email', 'password_hash', 'first_name', 'last_name', 'phone_number']] = \
            request.form['email'], request.form['password'], request.form['first_name'], request.form['last_name'], request.form['phone_number']
        save_user_data(user_data)
        flash('User updated successfully!', 'success')
        return redirect(url_for('admin.list_users'))
    return render_template("admin/edit_user.html", user=user)

@admin_bp.route("/users/delete/<int:user_id>")
def delete_user(user_id):
    user_data = load_user_data()
    user_data = user_data[user_data['user_id'] != user_id]
    save_user_data(user_data)
    flash('User deleted successfully!', 'success')
    return redirect(url_for('admin.list_users'))
