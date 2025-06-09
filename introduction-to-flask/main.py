from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>You are home</h1>"

@app.route('/<string:username>')
def user(username):
    return f"<h1>Profile for {username}</h1>"

if __name__ == '__main__':
    app.run(port=5555, debug=True)