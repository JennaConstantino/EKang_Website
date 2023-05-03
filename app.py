from flask import Flask, render_template, request

app = Flask(__name__)

@app.get('/')
def index():
    return render_template('index.html')


@app.get('/portfolio')
def portfolio():
    return render_template('portfolio.html')


@app.get('/curatorial')
def curatorial():
    return render_template('curatorial.html')