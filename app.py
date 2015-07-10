from flask import Flask, jsonify, make_response
import MySQLdb as mdb

MYSQL_HOST = 'localhost'
MYSQL_USER = 'particle'
MYSQL_PASSWORD = 'particle'
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

@app.route('/particle/devices', methods=['GET'])
def get_devices():
	try:
		con = mdb.connect(MYSQL_HOST, MYSQL_USER, MYSQL_PASSWORD, MYSQL_DATABASE)
		cur = con.cursor()
		cur.execute("SELECT * FROM devices")
		rows = cur.fetchall()
		response = []
		for row in rows:
			response.append({"id": row[1], "name": row[2]})
		return jsonify(devices=response)
	except:
		return make_response(jsonify({'error': 'No devices listed.'}), 404)

if __name__ == '__main__':
	app.run(debug=True)
