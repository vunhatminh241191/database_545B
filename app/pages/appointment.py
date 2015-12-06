from app.app import app, db

from flask import abort, jsonify, request
from flask import Flask, render_template

@app.route("/appointment", methods=['GET', 'POST'])
def appointment():
	if request.method == "GET":
		return render_template('appointment.html')

@app.route("/finding_appointment", methods=['GET', 'POST'])
def finding_appointment():
	if request.method == "POST":
		cursor = db.cursor()
		payment_id = request.form['text']
		cursor.execute("SELECT * from Appointment where appointment_sn=" + "'" + payment_id + "'")
		data = cursor.fetchone()
		if data is None:
			return render_template('appointment.html', not_found='This appointment does not exist')
		return render_template('appointment.html', data=data)
	if request.method == 'GET':
		return render_template('appointment.html')

@app.route("/making_new_appointment", methods=['GET', 'POST'])
def making_new_appointment():
	if request.method == "POST":
		return render_template('making_new_appointment')
	if request.method == "GET":
		return render_template('making_new_appointment')