from flaskApp import app
from flask import Flask, flash, render_template, redirect, request, session
from flaskApp.models.user import User
from flaskApp.models.post import Post
from flaskApp.models.likeComment import Comment

@app.route("/dashboard")
def dashboard():
    if 'userId' not in session:
        flash('Must be logged in to view this page')
        return redirect('/')
    postData={
        'id': session['userId']
    }
    commentData={
        'post_id': 5
    }
    posts=Post.getUsernameWithPost()
    comments=Comment.getCommentWithPost(commentData)
    return render_template('dashboard.html', user=User.getById(postData), posts=posts,comments=comments)


@app.route("/newPostPage")
def newPostPage():
    if 'userId' not in session:
        flash('Must be logged in to view this page')
        return redirect('/')
    data={
        "id": session['userId']
    }
    userId=session['userId']
    return render_template("newPostPage.html", user=User.getById(data),userId=userId)

@app.route('/newPost', methods=['POST'])
def newPost():
    if 'userId' not in session:
        flash('Must be logged in to view this page')
        return redirect('/')
    userId=session['userId']
    data={
        "image": request.form['formImageLink'],
        "description": request.form['formDescription'],
        "users_id": userId
    }
    
    Post.createPost(data)
    return redirect('/dashboard')


    
