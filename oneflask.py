from flask import Flask
app = Flask(__name__)

@app.route('/user/<username>')
def show_user_profile(username):
        return 'User %s' % username
    
@app.route('/post/<int:post_id>')    
def show_post(post_id):
    return 'Post %d!' % post_id


@app.route('/')
def constant():
    return """
    <p> Hello </p>
    <b> world </b>
    <i> Italics </i>
   """

@app.route('/index/')
def root():
    return app.send_static_file('index.html')

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
