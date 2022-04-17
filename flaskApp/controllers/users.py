from flaskApp import app
from flask import Flask, flash, render_template, redirect, request, session
from flaskApp.models.post import Post
from flaskApp.models.user import User
from flask_bcrypt import Bcrypt

bcrypt=Bcrypt(app)

@app.route("/")
def loginPage():
    return render_template('login.html')

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")

@app.route("/registrationPage")
def registrationPage():
    return render_template('registration.html')

@app.route('/register', methods=['POST'])
def register():
    if not User.validateUserRegistration(request.form):
        return redirect('/registrationPage')

    pwHash= bcrypt.generate_password_hash(request.form['formPassword'])
    print(pwHash)
    data={
        "firstName": request.form['formFirstName'],
        "lastName": request.form['formLastName'],
        "email": request.form['formEmail'],
        "password": pwHash
    }
    id=User.addUser(data)
    if not id:
        flash("something went wrong!")
        return redirect('/registration')
    session['userId']=id
    return redirect('/')

@app.route('/login',methods=['POST'])
def login():
    if not User.validateUserLogin(request.form):
        return redirect('/')
    data={"email": request.form['formEmail']}
    user= User.getLoginByEmail(data)
    if not user:
        flash("Invalid Login")
        return redirect('/')
    if not bcrypt.check_password_hash(user.password, request.form['formPassword']):
        flash("Invalid Login")
        return redirect('/')
    session['userId']= user.id
    return redirect('/dashboard')
    



