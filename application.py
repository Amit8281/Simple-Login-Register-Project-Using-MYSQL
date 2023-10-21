# application.py
from flask import Flask, render_template, request, redirect, url_for
from dbhelper import DBhelper

app = Flask(__name__)

class Flipkart:
    def __init__(self):
        # Connect to the database
        self.db = DBhelper()

# Create an instance of Flipkart
obj = Flipkart()

# Routes for login and register
@app.route('/')
def index():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    email = request.form['email']
    password = request.form['password']
    data = obj.db.search(email, password)
    if len(data) == 0:
        return "Incorrect Email/Password"
    else:
        return "Hello, " + data[0][1]

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        response = obj.db.register(name, email, password)
        if response == 1:
            return "Registration successful"
        else:
            return "Registration failed"
    # Handle GET request here, e.g., render the registration form
    return render_template('register.html')


if __name__ == '__main__':
    app.run(port=5000,debug=True)
