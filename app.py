#!/bin/python
from flask import Flask
import MySQLdb as mdb

MYSQL_HOST = 'localhost'
MYSQL_USER = 'root'
MYSQL_PASSWORD = ''
MYSQL_DATABASE = 'particle'

app = Flask(__name__)

@app.route('/')
def index():
	try:
		con = mdb.connect(MYSQL_HOST, MYSQL_USER, MYSQL_PASSWORD, MYSQL_DATABASE)
		cur = con.cursor()
		cur.execute("SELECT VERSION()")
		ver = cur.fetchone()
		return "Particle logging API. Database version: %s." % ver
	except:
		return "Particle logging API"

if __name__ == '__main__':
	app.run(debug=True)
