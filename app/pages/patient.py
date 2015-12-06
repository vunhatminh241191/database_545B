from app.app import app, db

from flask import abort, jsonify, request
from flask import Flask, render_template

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
		data = checking_user_account(cursor, list(cursor.fetchone()))
		if data == None:
			return render_template('patient.html', not_found="The result not found")
		return render_template('patient.html', data=data)
	if request.method == 'GET':
		return render_template('patient.html')

def checking_user_account(cursor, data):
	cursor.execute("SELECT * from Doctor where doctor_ssn=" + "'" + str(data[0])+ "'")
	current_data = cursor.fetchone()
	if current_data == None:
		return data
	else:
		return None