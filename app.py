from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return '<h1>Hello, World</h1>'

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