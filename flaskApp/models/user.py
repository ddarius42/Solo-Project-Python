from unittest import result
from flaskApp.config.mysqlconnection import connectToMySQL
from flask import flash

class Users:
    def __innit__(self,data):
        self.id =data['id']
        self.name =data['name']
        self.email =data['email']
        self.password =data['password']

    @classmethod
    def getAllUsers(cls,data):
        query="SELECT * FROM users;"
        results=connectToMySQL("pythonsoloproject").query_db(query)
        users=[]
        for user in users:
            users.append(cls(user))
        return users

    @classmethod
    def addUser(cls,data):
        query="INSERT INTO users(name,email,password,created_at, updated_at) Values(%(formName)s, %(formEmail)s, %(formPassword)s,now(),now())"
        return connectToMySQL('pythonsoloproject').query_db(query,data)