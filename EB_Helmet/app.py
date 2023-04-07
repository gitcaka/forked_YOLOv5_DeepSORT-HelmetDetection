from flask import Flask, render_template, Response
from flask_socketio import SocketIO

# init flask
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'

# init source and format
savedir = 'D:/#Data/Detect/'
format = '.jpg'

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=False)