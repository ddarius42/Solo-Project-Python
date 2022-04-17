
from flaskApp.config.mysqlconnection import connectToMySQL
from flask import flash

import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

from flaskApp import app
from flask_bcrypt import Bcrypt        
bcrypt = Bcrypt(app)  

class User:
    def __init__(self,data):
        self.id = data['id']
        self.firstName = data['firstName']
        self.lastName = data['lastName']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


    @classmethod
    def getAllUsers(cls):
        query="SELECT * FROM users;"
        results=connectToMySQL("pythonsoloproject").query_db(query)
        users=[]
        for user in results:
            users.append(cls(user))
        return users
    
    @classmethod
    def getById(cls,data):
        query="SELECT * FROM users where id = %(id)s;"
        results= connectToMySQL('pythonsoloproject').query_db(query,data)
        if len(results)<1:
            return False
        return (cls(results[0]))

    @classmethod
    def getLoginByEmail(cls,data):
        query="SELECT * FROM users WHERE email = %(email)s;"
        results = connectToMySQL('pythonsoloproject').query_db(query,data)
        if len(results)<1:
            return False
        return (cls(results[0]))

    @classmethod
    def addUser(cls,data):
        query="INSERT INTO users(firstName,lastName,email,password,created_at, updated_at) Values(%(firstName)s,%(lastName)s, %(email)s, %(password)s,now(),now())"
        return connectToMySQL('pythonsoloproject').query_db(query,data)

    @staticmethod
    def validateUserRegistration(user):
        isValid=True
        query="SELECT * FROM users WHERE email = %(formEmail)s;"
        results = connectToMySQL('pythonsoloproject').query_db(query, user)
        if len(results)>=1:
            flash('email already exists!')
            isValid= False
        if not EMAIL_REGEX.match(user['formEmail']):
            flash('Invalid email address please try again!!!')
            isValid=False
        if len(user['formFirstName']) < 2:
            flash("First Name needs to contain at least 2 lettters.")
            isValid=False
        if len(user['formLastName'])<2:
            flash("Last Name needs to contain at least 2 lettters.")
            isValid=False
        if len(user['formPassword']) < 8:
            flash("Password must contain at least 8 characters long")
            isValid = False
        if user['formPassword'] != user['confirmPassword']:
            flash("Passwords did not match")
            isValid=False
        if isValid ==True:
            flash("Sign Up Success")
        return isValid


    @staticmethod
    def validateUserLogin(user):
        isValid=True
        if not EMAIL_REGEX.match(user['formEmail']):
            flash('Invalid email address please try again!!!')
            isValid=False
        if len(user['formPassword']) < 8:
            flash("Password must contain at least 8 characters long")
            isValid = False
        return isValid