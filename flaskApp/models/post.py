from flaskApp.config.mysqlconnection import connectToMySQL
from flask import flash

class Post:
    def __init__(self,data):
        self.id = data['id']
        self.image = data['image']
        self.description = data['description']
        self.users_id = data['users_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def getAllPosts(cls):
        query="SELECT * FROM posts;"
        results=connectToMySQL("pythonsoloproject").query_db(query)
        posts=[]
        for post in results:
            posts.append(cls(post))
        return posts

    @classmethod
    def createPost(cls, data):
        query="INSERT INTO posts (image,description,created_at,updated_at,users_id) VALUES(%(image)s,%(description)s,now(),now(),%(users_id)s);"
        return connectToMySQL("pythonsoloproject").query_db(query,data)


    @classmethod
    def getUsernameWithPost(cls):
        query="SELECT * FROM posts LEFT JOIN users ON posts.users_id WHERE users_id= users.id;;"
        results=connectToMySQL("pythonsoloproject").query_db(query)
        leftJoined=[]
        for allDetails in results:
            leftJoined.append(allDetails)
        return leftJoined


