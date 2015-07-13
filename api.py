from flask import Flask, jsonify, make_response, request
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

@app.route('/devices', methods=['GET'])
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

@app.route('/events', methods=['GET'])
def get_events():
	start = request.args.get('start')
	num_rows = request.args.get('num_rows')
	try:
		con = mdb.connect(MYSQL_HOST, MYSQL_USER, MYSQL_PASSWORD, MYSQL_DATABASE)
		cur = con.cursor()
		cur.execute("SELECT * FROM events LIMIT " + str(int(start) - 1) + ", " + num_rows)
		response = []
		for i in range(0, int(num_rows)):
			row = cur.fetchone()
			response.append({"id": row[0], "device": row[2], "data": row[3]})
		return jsonify(events=response)
	except:
		return make_response(jsonify({'error': 'No event data returned'}), 404)

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=8080)
