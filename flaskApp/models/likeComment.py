from flaskApp.config.mysqlconnection import connectToMySQL
from flask import flash

class Comment:
    def __init__(self,data):
        self.commentId = data['commentId']
        self.comment = data['comment']
        self.user_id = data['user_id']
        self.post_id = data['post_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

        self.posts=[]

    @classmethod
    def createComment(cls,data):
        query="INSERT INTO comments(comment, user_id, post_id, created_at, updated_at) VALUES(%(comment)s,%(user_id)s,%(post_id)s,now(),now());"
        return connectToMySQL('pythonsoloproject').query_db(query,data)

    @classmethod
    def getCommentWithPost(cls):
        query="SELECT * FROM comments LEFT JOIN posts on comments.commentId LEFT JOIN users ON comments.commentId WHERE comments.user_id = users.id AND comments.post_id = posts.id AND post_id =posts.id;"
        results=connectToMySQL('pythonsoloproject').query_db(query)
        leftJoined=[]
        for result in results:
            leftJoined.append(result)
        return leftJoined