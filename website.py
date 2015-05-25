import os
from flask import Flask, render_template

app = Flask(__name__)




@app.route('/')
@app.route('/index/')
def about():
    return render_template('index.html')
    
if __name__ == '__main__':
	app.debug = True
	app.run(host = '0.0.0.0', port = 5000)