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
	try:
		start = request.args.get('start')
		num_rows = request.args.get('num_rows')
	except:
		start = None
		num_rows = None
	try:
		device = request.args.get('device')
	except:
		device = None
	try:
		start_date = request.args.get('start_date')
		end_date = request.args.get('end_date')
	except:
		start_date = None
		end_date = None
	
	try:
		con = mdb.connect(MYSQL_HOST, MYSQL_USER, MYSQL_PASSWORD, MYSQL_DATABASE)
		cur = con.cursor()
		
		if (device != None):
			if (start_date != None):
				query = "SELECT * FROM events WHERE device='" + device + "' AND timestamp BETWEEN '" + start_date + "' AND '" + end_date + "'"
			else:
				query = "SELECT * FROM events WHERE device='" + device + "' LIMIT "  + str(int(start) - 1) + ", " + num_rows
		else:
			query = "SELECT * FROM events LIMIT " + str(int(start) - 1) + ", " + num_rows
		
		cur.execute(query)
		
		response = []
		if (num_rows != None):
			for i in range(0, int(num_rows)):
				row = cur.fetchone()
				response.append({"id": row[0], "timestamp": str(row[1]), "device": row[2], "data": row[3]})
		else:
			rows = cur.fetchall()
			for row in rows:
				response.append({"id": row[0], "timestamp": str(row[1]), "device": row[2], "data": row[3]})
		
		return jsonify(events=response)
	except:
		return make_response(jsonify({'error': 'No event data returned'}), 404)

@app.route('/measurements', methods=['GET'])
def get_measurements():
	try:
		start_date = request.args.get('start_date')
		end_date = request.args.get('end_date')
	except:
		start_date = None
		end_date = None
	device = request.args.get('device')
	measurement = request.args.get('measurement')
	try:
		con = mdb.connect(MYSQL_HOST, MYSQL_USER, MYSQL_PASSWORD, MYSQL_DATABASE)
		cur = con.cursor()
		if (start_date != None):
			query = "SELECT * FROM events WHERE device='" + device + "' AND measurement='" + measurement + "' AND timestamp BETWEEN '" + start_date + "' AND '" + end_date + "'"
		else :
			query = "SELECT * FROM events WHERE device='" + device + "' AND measurement='" + measurement + "'"
		cur.execute(query)
		response = []
		rows = cur.fetchall()
		for row in rows:
			response.append({"id": row[0], "timestamp": str(row[1]), "device": row[2], "measurement": row[4], "value": row[5]})
		return jsonify(measurements=response)
	except:
		return make_response(jsonify({'error': 'No measurement data returned'}), 404)

@app.route('/analyses', methods=['GET'])
def get_analyses():
	try:
		start_date = request.args.get('start_date')
		end_date = request.args.get('end_date')
	except:
		start_date = None
		end_date = None
	room = request.args.get('room')
	name = request.args.get('name')
	try:
		con = mdb.connect(MYSQL_HOST, MYSQL_USER, MYSQL_PASSWORD, MYSQL_DATABASE)
		cur = con.cursor()
		if (start_date != None):
			query = "SELECT * FROM analyses WHERE room='" + room + "' AND name='" + name + "' AND timestamp BETWEEN '" + start_date + "' AND '" + end_date + "'"
		else :
			query = "SELECT * FROM analyses WHERE room='" + room + "' AND name='" + name + "'"
		cur.execute(query)
		response = []
		rows = cur.fetchall()
		for row in rows:
			response.append({"id": row[0], "timestamp": str(row[1]), "room": row[2], "name": row[3], "value": row[4]})
		return jsonify(measurements=response)
	except:
		return make_response(jsonify({'error': 'No analysis data returned'}), 404)

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=8080)
