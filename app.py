"""
This script runs the application using a development server.
It contains the definition of routes and views for the application.
"""

from flask import Flask, render_template, request
app = Flask(__name__)

# Make the WSGI interface available at the top level so wfastcgi can get it.
wsgi_app = app.wsgi_app


@app.route('/', methods=['POST', 'GET'])
def index():
    background = 'White'
    font = 'Black'
    bgColors = ['Red', 'Blue', 'Green']
    fColors = ['Yellow', 'Purple', 'Black']
    if request.method == 'POST':
        background = request.form['background']
        font = request.form['font']
    return render_template('index.html', bgColors=bgColors, fColors=fColors, background=background, font=font)

if __name__ == '__main__':
    import os
    HOST = os.environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(os.environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    app.run(HOST, PORT)
