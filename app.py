from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return "Welcome to Dan's API"

@app.route('/welcome/<name>')
def welcome(name):
    return 'Welcome ' + name

@app.route('/earth')
def earth():
    return 'The circumference of the earth is 40,075km'

if __name__ == '__main__':
    app.run()