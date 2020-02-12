from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def root():
    return render_template('index.html')