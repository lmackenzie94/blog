from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

user = {'firstname': 'admin',
        'lastname': 'user',
        'username': 'admin',
        'password': 'admin123'}

def valid_login(username, password):
    if username == user['username'] and password == user['password']:
        return True
    
    return False

@app.route('/', methods=['POST', 'GET'])
def index():
    error = None

    if request.method == 'POST':
        if valid_login(request.form['username'],
                       request.form['password']):
            return log_user_in(request.form['username'])
        else:
            error = "Invalid username/password."

    return render_template('index.html', error=error)

@app.route('/dashboard', methods=['POST', 'GET'])
def dashboard():
    error = None

    return render_template('dashboard.html', error=error)

@app.route('/register', methods=['POST', 'GET'])
def register():
    error = None

    if request.method == 'POST':
         if valid_register(request.form['username'],
                           request.form['password'],
                           request.form['repeat_password'],
                           request.form['firstname'],
                           request.form['lastname']):
             return log_user_in(request.form['username'])
         else:
             error = 'Invalid register. Figure it out.'

    return render_template('register.html', error=error)
