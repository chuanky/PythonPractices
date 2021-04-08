from flask import Flask
from flask import request
app = Flask(__name__)

@app.route('/')
def hello_world():
  return 'Hello, World!'

@app.route('/post/<int:post_id>')
def show_post(post_id):
  # 调用其他python代码
  # show the post with the given id, the id is an integer
  return 'Post %d' % post_id

@app.route('/post', methods=['POST'])
def post_request():
  # 调用其他python代码
  # show the post with the parameter
  return 'Post parameters: ' + str(request.args['post_title'])