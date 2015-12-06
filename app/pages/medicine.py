from app.app import app, db

from flask import abort, jsonify, request
from flask import Flask, render_template

@app.route("/medicine", methods=['GET', 'POST'])
def medicine():
	if request.method == 'GET':
		return render_template('medicine.html')

@app.route("/finding_medicine", methods=['GET', 'POST'])
def finding_medicine():
	if request.method == 'GET':
		return render_template('medicine.html')
	elif request.method == 'POST':
		medicine_name = request.form['medicine_name']
		type_of_medicine_shape = request.form['type_of_medicine_shape']
		producer = request.form['medicine_company']

		# db cursor
		cursor = db.cursor()

		if producer == '' or type_of_medicine_shape == '' or medicine_name == '':
			return render_template('medicine.html', not_found='Please input enough information that helps us find the result')
		cursor.execute("SELECT * from Medicine where medicine_name='" + medicine_name + "' and producer='" + producer + "' and shape='" + type_of_medicine_shape + "' ")
		medicine = cursor.fetchone()
		if medicine == None:
			return render_template('medicine.html', not_found='The result is not found')
		else:
			return render_template('medicine.html', data=medicine)