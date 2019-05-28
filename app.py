from flask import Flask, render_template, request

app = Flask(__name__)

crows_count = 100500

@app.route('/')
def index():
    return render_template('index.html', crows_count=crows_count)

@app.route('/count', methods=['GET', 'POST'])
def count():
    global crows_count
    if request.method == 'POST':
        crows_count+=1
    return render_template('count.html', crows_count=crows_count)