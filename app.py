from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return "Welcome to Dan's API"

@app.route('/welcome/<name>')
def welcome(name):
    return 'Welcome ' + name

if __name__ == '__main__':
    app.run()