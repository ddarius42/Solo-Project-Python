from flaskApp import app
from flask import Flask, flash, render_template, redirect, request, session
from flaskApp.models.user import Users

@app.route("/")
def login():
    return render_template('login.html')