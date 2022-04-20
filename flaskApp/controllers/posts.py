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
    userData={
        'id': session['userId']
    }
    posts=Post.getUsernameWithPost()
    comments=Comment.getCommentWithPost()
    return render_template('dashboard.html', user=User.getById(userData), posts=posts,comments=comments)


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

@app.route('/profile')
def liked():
    if 'userId' not in session:
        flash('Must be logged in to view this page')
        return redirect('/')
    data={
        "users_id": session['userId']
    }
    userData={
        'id': session['userId']
    }
    userPost=Post.getPostByUser(data)
    return render_template('profile.html',userPost=userPost, user=User.getById(userData),)


@app.route('/editPostPage/<postId>')
def editPostPage(postId):
    
    data={
        "postId": postId
    }
    postById=Post.getPostById(data)
    return render_template('editPost.html',postById=postById)

@app.route('/editPost/<postId>', methods=['POST'])
def editPost(postId):
    data={
        "postId": postId,
        "postDescription": request.form['formDescription']
    }
    Post.updatePost(data)
    return redirect('/profile')

@app.route('/deletePost/<postId>')
def deletePost(postId):
    data={
        "postId": postId
    }
    Post.deletePost(data)
    return redirect('/profile')