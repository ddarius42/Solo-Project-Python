from flaskApp import app
from flaskApp.controllers import users
from flaskApp.controllers import posts
from flaskApp.controllers import likesComments

if __name__ == "__main__":
    app.run(debug=True)