from flask                             import request
from flask_api                         import FlaskAPI
from src.views.home.home               import renderHome
from src.views.login.login             import renderLogin
from src.api.threads.threadsBlockPosts import apiThreadsBlockPosts

app = FlaskAPI(__name__)

# Global variable to store database in memory
#app.Objects = []

@app.route('/')
def home():
  return renderHome()

@app.route("/api/threads/blockposts", methods = ['GET'])
def threadBlockPosts():
  #return ['Hello world']
  return apiThreadsBlockPosts();

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