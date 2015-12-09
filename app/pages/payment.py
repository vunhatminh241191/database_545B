from app.app import app, db

from flask import abort, jsonify, request
from flask import Flask, render_template

@app.route("/payment", methods=['GET', 'POST'])
def payment():
	if request.method == "GET":
		return render_template('payment.html')

@app.route("/finding_payment", methods=['GET', 'POST'])
def finding_payment():
	if request.method == "POST":
		cursor = db.cursor()
		payment_id = request.form['text']
		cursor.execute("SELECT * from Payment where appointment_sn=" + "'" + payment_id + "'")
		data = cursor.fetchone()
		if data is None:
			return "huhu"
		return render_template('payment.html', data=data)