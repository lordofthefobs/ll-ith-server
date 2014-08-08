#!/usr/bin/env python

from flask import Flask, render_template
from jinja2 import ChoiceLoader, FileSystemLoader

app = Flask(__name__)

app.debug = True

my_loader = ChoiceLoader([
	app.jinja_loader,
	FileSystemLoader('dist')
])	

app.jinja_loader = my_loader

@app.route('/')
def index():
	return render_template("index.html")

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5001)