from app.app import app, db

from flask import abort, jsonify, request, json
from flask import Flask, render_template

import datetime

@app.route("/patient", methods=['GET', 'POST'])
def patient():
	if request.method == "GET":
		return render_template('patient.html')

@app.route("/finding_patient", methods=['POST', 'GET'])
def finding_patient():
	if request.method == "POST":
		if request.form['search_string'] == '':
			return render_template('patient.html', not_found="Please input user's email to search")
		cursor = db.cursor()
		cursor.execute("SELECT * from User where email=" + "'" + request.form['search_string'] + "'")
		data = cursor.fetchone()
		if data == None:
			return render_template('patient.html', not_found="The result not found")
		return render_template('patient.html', data=data)
	if request.method == 'GET':
		return render_template('patient.html')

@app.route("/creating_new_account", methods=['GET', 'POST'])
def creating_new_account():
	return render_template('adding_new_patient.html')

@app.route("/adding_account", methods=['GET', 'POST'])
def adding_account():
	if request.method == 'POST':
		ssn = request.form['patient_ssn']
		first_name = request.form['patient_first_name']
		last_name = request.form['patient_last_name']
		age = request.form['patient_age']
		email = request.form['patient_email']
		address = request.form['patient_address']
		city = request.form['patient_city']
		state = request.form['patient_state']
		zipcode = request.form['patient_zipcode']
		phone = request.form['patient_phone_number']
		date_of_birth = request.form['patient_date_of_birth']

		cursor = db.cursor()
		cursor.execute("""INSERT INTO User VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, null)""", (str(ssn)
			, str(first_name), str(last_name), str(age), str(email), str(address)
			, str(city), str(state), str(zipcode), str(phone), str(date_of_birth)))

		cursor.execute("""INSERT INTO Patient VALUES (%s)""", (str(ssn), ))

		db.commit()
		return render_template('new_account.html', data_return=[ssn
			, first_name, last_name, age, email, address, city, state, zipcode, phone, date_of_birth])
	else:
		return render_template('adding_new_patient.html')

def checking_user_account(cursor, data):
	cursor.execute("SELECT * from Doctor where doctor_ssn=" + "'" + str(data[0])+ "'")
	if current_data == None:
		return data
	else:
		return None

def checking_patient_account(patient_ssn):
	cursor = db.cursor()
	cursor.execute("SELECT * from User where ssn=" + "'" + patient_ssn + "'")
	data = cursor.fetchone()
	if data == None:
		return True
	else:
		return False


