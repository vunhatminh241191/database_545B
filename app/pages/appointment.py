from app.app import app, db

from flask import abort, jsonify, request, url_for, json
from flask import Flask, render_template, redirect, session

from patient import checking_patient_account

import datetime

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
		return render_template('making_new_appointment.html')
	elif request.method == "GET":
		return render_template('making_new_appointment.html')

@app.route("/create_appointment", methods=['GET', 'POST'])
def create_appointment():
	if request.method == 'GET':
		return render_template('making_new_appointment.html')
	elif request.method == 'POST':
		patient_ssn = request.form['patient_ssn']
		symptoms = request.form['symptoms']

		if patient_ssn == '' or symptoms == '':
			return render_template('making_new_appointment.html')

		elif checking_patient_account(patient_ssn):
			messages = json.dumps({'patient_ssn':patient_ssn})
			return redirect(url_for(".creating_new_account", messages=messages))

		else:
			add_appointment_to_database(db.cursor(), patient_ssn, symptoms)
			return render_template('making_new_appointment.html', data='Doctor will see you in the moment')

def add_appointment_to_database(cursor, patient_ssn, symptoms):
	# finding min appointment number 
	cursor.execute("SELECT max(appointment_sn) from Appointment")
	max_appointment_number = cursor.fetchone()
	current_appointment_number = int(max_appointment_number[0]) + 1
	today = datetime.datetime.now()
	cursor.execute("""INSERT INTO Appointment VALUES (%s, null, %s, %s, %s, null )"""
		,(str(current_appointment_number), patient_ssn, symptoms, today.strftime("%m-%d-%Y")))
	db.commit()

