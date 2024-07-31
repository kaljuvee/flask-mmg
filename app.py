from flask import Flask, render_template, request, redirect, url_for, flash
import pandas as pd

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # Needed for flash messages

# Function to save user data to a CSV file (you can use a database instead)
def save_user_data(user_data):
    user_data_df = pd.DataFrame(user_data, index=[0])
    try:
        existing_data = pd.read_csv('user_data.csv')
        updated_data = pd.concat([existing_data, user_data_df], ignore_index=True)
    except FileNotFoundError:
        updated_data = user_data_df
    updated_data.to_csv('user_data.csv', index=False)

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        try:
            existing_data = pd.read_csv('user_data.csv')
            user = existing_data[(existing_data['Email'] == email) & (existing_data['Password'] == password)]
            if not user.empty:
                flash('Sign In successful!', 'success')
                return redirect(url_for('account'))
            else:
                flash('Invalid email or password.', 'danger')
        except FileNotFoundError:
            flash('Could not find the user. Please sign up first.', 'danger')
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']
        password = request.form['password']
        confirm_password = request.form['confirm_password']
        
        if password == confirm_password:
            user_data = {
                'First Name': first_name,
                'Last Name': last_name,
                'Email': email,
                'Password': password
            }
            save_user_data(user_data)
            flash('Sign Up successful!', 'success')
            return redirect(url_for('account'))
        else:
            flash('Passwords do not match.', 'danger')
    return render_template('register.html')

@app.route('/account')
def account():
    return 'My Account Page'

if __name__ == '__main__':
    app.run(debug=True)
