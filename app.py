import sqlite3
import flask
from sqlite3 import Error
from contextlib import closing
from flask import Flask, render_template, request
app = Flask(__name__)

# Make the WSGI interface available at the top level so wfastcgi can get it.
wsgi_app = app.wsgi_app


@app.route('/', methods=['POST', 'GET'])
def index():
    background = 'White'
    font = 'Black'
    bgColors = getColors()
    fColors = getColors()
    if request.method == 'POST':
        background = request.form['background']
        font = request.form['font']
    return render_template('index.html', bgColors=bgColors, fColors=fColors, background=background, font=font)

def connectdb():
    conn = sqlite3.connect('Colors.db', check_same_thread=False)
    return conn

def countColors():
    conn = connectdb()
    c = conn.cursor()
    colorCount = '''SELECT * FROM Colors'''
    c.execute(colorCount)
    colorCounter = len(c.fetchall())
    c.close()
    return colorCounter

def getColors():
    colors = []
    x = 0
    i = countColors()
    conn = connectdb()
    c = conn.cursor()
    query = '''SELECT Color FROM Colors'''
    c.execute(query)
    while x < i:
        color = c.fetchone()
        colors.append(color[0])
        x += 1
    c.close()
    return colors




if __name__ == '__main__':
    import os
    HOST = os.environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(os.environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    app.run(HOST, PORT)
    
