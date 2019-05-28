from flask import Flask, render_template

app = Flask(__name__)

crows_count = 100500

@app.route('/')
def index():
    return render_template('index.html', crows_count=crows_count)