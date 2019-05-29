from flask import Flask, render_template, request, jsonify
from flask_socketio import SocketIO, emit

app = Flask(__name__)
socketio = SocketIO(app)

app.config['SECRET_KEY'] = 'secret!'

crows_count = 100500

@app.route('/')
def index():
    return render_template('index.html', crows_count=crows_count)

@app.route('/count', methods=['GET', 'POST'])
def count():
    global crows_count
    if request.method == 'POST':
        crows_count += 1
    return render_template('count.html', crows_count=crows_count)

@app.route('/add_crow', methods=['POST'])
def add_crow():
    global crows_count
    crows_count += 1
    return jsonify({'crows_count': crows_count})

@socketio.on("add crow")
def add():
    global crows_count
    crows_count += 1
    print("crow added")
    emit('crow added', {'crows_count': crows_count}, broadcast=True)   