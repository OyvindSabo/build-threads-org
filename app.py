from flask import Flask
from src.views.home.home import renderHome
from src.views.login.login import renderLogin
app = Flask(__name__)

@app.route('/')
def home():
    return renderHome()

# Login
@app.route('/login')
def showLogin():
  return renderLogin()

# User profile
@app.route('/user/<username>')
def showUserProfile(username):
    print(username)
    return f'User {username}'

# All forums
@app.route('/forums/')
def showForums():
    return 'Forums'

# Forum
@app.route('/forums/<forumName>/')
def showForum(forumName):
    return f'Forum {forumName}'

# Forum thread
@app.route('/forums/<forumName>/<username>/')
def showPost(forumName, username):
    return f'Post {forumName}, {username}'