from flask import Flask, session
from flask import render_template
from flask import request
from flask import redirect
import json

app = Flask(__name__)
app.secret_key = 'meow'

@app.route('/')
def index():
    user_logged_in = session.get('logged_in', False)
    return render_template('index.html', user_logged_in=user_logged_in)

@app.route('/login')
def login():
    if session.get('logged_in', False):
        # User is already logged in, redirect to the homepage
        return redirect('/')
    return render_template('login.html')

email = None

@app.route('/login_form', methods=['post'])
def login_form():
    global email
    email = request.form.get('email')
    username = request.form.get('username')
    password = request.form.get('password')
    password_confirmation = request.form.get('password_confirmation')
    
    if email == 'example@example.com' and password == 'password':
        session['logged_in'] = True
    else:
        session['logged_in'] = False
    return redirect("/")

@app.route('/logout')
def logout():
    session['logged_in'] = False
    return redirect('/')

@app.route('/product1')
def product1():
    return render_template('product1.html')

@app.route('/product2')
def product2():
    return render_template('product2.html')

@app.route('/product3')
def product3():
    return render_template('product3.html')

if __name__ == '__main__':
    app.run(debug=True)
