from app.app import app, db

from flask import abort, jsonify, request
from flask import Flask, render_template

@app.route("/doctor", methods=['GET', 'POST'])
def doctor():
	if request.method == "GET":
		return render_template('doctor.html')

@app.route("/finding_doctor", methods=['POST', 'GET'])
def finding_doctor():
	if request.method == "POST":
		if request.form['search_string'] == '':
			return render_template('doctor.html', not_found="Please input email or doctor's license number to search")
		cursor = db.cursor()
		if request.form['type_of_search'] == 'email':
			cursor.execute("SELECT * from User where email=" + "'" + request.form['search_string'] + "'")
			current_data = cursor.fetchone()
			if current_data is None:
				return render_template('doctor.html', not_found='The result is not found')
			else:
				final_data = finding_missing_data(cursor, current_data, 1)
		else:
			cursor.execute("SELECT * from Doctor where doctor_licensing_number=" + "'" + request.form['search_string'] + "'")
			current_data = cursor.fetchone()
			if current_data is None:
				return render_template('doctor.html', not_found='The result is not found')
			else:
				final_data = finding_missing_data(cursor,current_data , 2)
		return render_template('doctor.html', data=final_data)
	if request.method == 'GET':
		return render_template('doctor.html')

def finding_missing_data(cursor, data, missing_type):
	data = list(data)
	if missing_type == 1:
		cursor.execute("SELECT * from Doctor where doctor_ssn=" + "'" + str(data[0])+ "'")
		data.insert(1, cursor.fetchone()[1])
		return data
	else:

		cursor.execute("SELECT * from User where ssn=" + "'" + str(data[0]) + "'")
		missing_data = cursor.fetchone()
		data.extend(missing_data)
		del data[2]
		return data

