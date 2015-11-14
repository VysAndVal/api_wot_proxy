"""
The flask application package.
"""

from flask import request
from flask import Response
import flask
import urllib.request as web

app = flask.Flask(__name__)

@app.route('/', methods=['POST'])
def home():
	return "hello"
	'''
	url = request.form['a']
	bla = web.urlopen(url).readall().decode('utf-8')
	return Response(response=bla, status=200, mimetype="application/json")'''


