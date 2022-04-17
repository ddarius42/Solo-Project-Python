
from flaskApp import app
from flask import Flask, flash, render_template, redirect, request, session
from flaskApp.models.user import User
from flaskApp.models.post import Post
from flaskApp.models.likeComment import Comment

@app.route('/comment/<userId>', methods=['POST'])
def comment(userId):
    data={
        "comment": request.form['formComment'],
        "user_id": userId,
        "post_id": request.form['formPostId']
    }
    Comment.createComment(data)
    return redirect('/dashboard')