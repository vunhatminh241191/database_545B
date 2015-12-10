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
		appointment = request.form['text']
		checking, data = getting_all_appointment_info(appointment)
		if checking == False:
			return render_template('appointment.html', not_found=data)
		else:
			return render_template('showing_appointment.html', data=data)
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
			appointment_number = add_appointment_to_database(db.cursor(), patient_ssn, symptoms)
			return render_template('making_new_appointment.html', data=appointment_number)

@app.route("/delete_appointment", methods=['GET', 'POST'])
def delete_appointment():
	if request.method == 'GET':
		return render_template('delete_appointment.html')
	elif request.method == 'POST':
		cursor = db.cursor()
		appointment_number = request.form['appointment_number']
		cursor.execute("SELECT * from Appointment where appointment_sn=(%s)", (appointment_number, ))
		data = cursor.fetchone()
		if data == None:
			return render_template('delete_appointment.html', data='Appointment did not exist')
		elif data[1] != None:
			return render_template('delete_appointment.html', data='You can not delete this appointment')
		else:
			cursor.execute("DELETE FROM Appointment Where appointment_sn=(%s)" , (appointment_number, ))
			db.commit()
			return render_template('delete_appointment.html', data="We apologizes when we could not help you. Hope you will get well sone!!!")

@app.route("/showing_appointment_update_info/<appointment>/<set_value>", methods=['GET', 'POST'])
def showing_appointment_update_info(appointment, set_value):
	if request.method == 'GET':
		checking, return_data = getting_all_appointment_info(appointment)
		return_data.append(set_value)
		return render_template('update_appointment.html', data=return_data)

@app.route("/update_appointment/<appointment>", methods=['GET', 'POST'])
def update_appointment(appointment):
	if request.method == "POST":
		cursor = db.cursor()

		symptoms = request.form['symptoms']
		notes = request.form['notes']
		if len(request.form) <= 3:
			# update appointment info
			cursor.execute("UPDATE Appointment set symptoms=%s, notes=%s where appointment_sn=%s", (symptoms, notes, appointment))
			db.commit()
		else:
			medicine_name = request.form['medicine_name']
			medicine_shape = request.form['medicine_shape']
			medicine_producer = request.form['medicine_producer']
			medicine_unit_per_time = request.form['medicine_unit_per_time']
			medicine_total = request.form['medicine_total']

			# checking existing medicine
			cursor.execute("SELECT * from Medicine where medicine_name=%s and shape=%s and producer=%s"
				, (medicine_name, medicine_shape, medicine_producer))
			medicine_info = cursor.fetchone()
			if medicine_info == None:
				return redirect(url_for('showing_appointment_update_info', appointment=appointment, set_value=1))
			else:
				cursor.execute("UPDATE Appointment_medicine set medicine_name=%s, shape=%s, producer=%s where appointment_sn=%s"
					, (medicine_name, medicine_shape, medicine_producer, appointment))
				db.commit()
		checking, return_data = getting_all_appointment_info(appointment)
		return render_template('showing_appointment.html', data=return_data)

def add_appointment_to_database(cursor, patient_ssn, symptoms):
	# finding min appointment number 
	cursor.execute("SELECT max(appointment_sn) from Appointment")
	max_appointment_number = cursor.fetchone()
	current_appointment_number = int(max_appointment_number[0]) + 1
	today = datetime.datetime.now()
	cursor.execute("""INSERT INTO Appointment VALUES (%s, null, %s, %s, %s, null )"""
		,(str(current_appointment_number), patient_ssn, symptoms, today.strftime("%m-%d-%Y")))
	db.commit()
	return current_appointment_number

def getting_all_appointment_info(appointment):
	cursor = db.cursor()
	# appointment information
	cursor.execute("SELECT * from Appointment where appointment_sn=(%s)", (appointment, ))
	appointment_info = cursor.fetchone()
	if appointment_info == None:
		return False, "This appointment does not exist"
	else:
		return_data = [str(x) for x in appointment_info]

	# medicine of appointment information
	cursor.execute("SELECT * from Appointment_medicine where appointment_sn=(%s)", (appointment, ))
	appointment_medicine_info = cursor.fetchone()
	if appointment_medicine_info == None:
		return True, return_data
	else:	
		return_data.extend([str(x) for x in appointment_medicine_info[1:]])
	return True, return_data
