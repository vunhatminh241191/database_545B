from Tkinter import *
import tkMessageBox
import pymysql
import datetime


class Appointment:

	def clearInfoFrame(self):
		for widget in self.infoFrame.winfo_children():
			widget.destroy()
		return

	def doMakeAppointment(self, data):
		conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='', db='FinalProject')
		cur = conn.cursor()
		print("doMakeAppointment")
		print(data)
		try:
			cur.execute("SELECT MAX(appointment_sn) FROM Appointment;")
			sn=0
			for row in cur:
				sn=int(row[0])+1
				print("new appointment_sn is %d"%sn)
			now = datetime.datetime.now()
			date = "%d-%d-%d"%(now.year,now.month,now.day)
			print("INSERT INTO Appointment VALUES ('%d', '100000008', '%s', '%s', '%s', '');"%(sn, data[0], data[1], date))
			cur.execute("INSERT INTO Appointment VALUES ('%d', '100000008', '%s', '%s', '%s', '');"%(sn, data[0], data[1], date))
			conn.commit()
			tkMessageBox.showinfo("^_^","Success! Appointment SN is %d"%(sn))
			self.clearInfoFrame()
		except:
			self.msgErr(1)
			self.makeNewUser(data)

		conn.close()
		return

	def makeAppointment(self):
		self.clearInfoFrame()
		fMAInput = Frame(self.infoFrame, width=890, height=300)
		fMAInput.pack(fill=BOTH, side=TOP)	
		
		lSsn = Label(fMAInput, text="SSN")
		lSsn.grid(column=0, row=0)
		eSsn = Entry(fMAInput, width=30)
		eSsn.grid(column=1, row=0)

		lSymptom = Label(fMAInput, text="Symtoms")
		lSymptom.grid(column=0, row=3)
		eSymptom = Entry(fMAInput, width=30)
		eSymptom.grid(column=1, row=3)

		data=[]
		data.append(eSsn)
		data.append(eSymptom)

		bSubmit = Button(fMAInput, text="Submit", command=lambda: self.doMakeAppointment([x.get() for x in data]))
		bSubmit.grid(columnspan=2, column=0, row=8)

		return

	def makeNewUser(self, data):
		self.clearInfoFrame()

		fMAInput = Frame(self.infoFrame, width=890, height=300)
		fMAInput.pack(fill=BOTH, side=TOP)
		
		lSsn = Label(fMAInput, text="SSN")
		lSsn.grid(column=0, row=0)
		eSsn = Entry(fMAInput, width=30)
		eSsn.grid(column=1, row=0)

		lBirthdate = Label(fMAInput, text="Birthdate")
		lBirthdate.grid(column=0, row=1)
		eBirthdate = Entry(fMAInput, width=30)
		eBirthdate.grid(column=1, row=1)

		lPhone = Label(fMAInput, text="Phone Number")
		lPhone.grid(column=0, row=2)
		ePhone = Entry(fMAInput, width=30)
		ePhone.grid(column=1, row=2)


		if data :
			print(data)
			# vSymptom = String()
			lSymptom = Label(fMAInput, text="Symtoms")
			lSymptom.grid(column=0, row=3)
			eSymptom = Entry(fMAInput, width=30)
			eSymptom.grid(column=1, row=3)
			eSsn.insert(0,data[0])
			eSymptom.insert(0,data[1])
		
		lFirstName = Label(fMAInput, text="First Name")
		lFirstName.grid(column=0, row=4)
		eFirstName =Entry(fMAInput, width=30)
		eFirstName.grid(column=1, row=4)
		lLastName = Label(fMAInput, text="Last Name")
		lLastName.grid(column=0, row=5)
		eLastName =Entry(fMAInput, width=30)
		eLastName.grid(column=1, row=5)
		lAddr = Label(fMAInput, text="Address")
		lAddr.grid(column=0, row=6)
		eAddr =Entry(fMAInput, width=30)
		eAddr.grid(column=1, row=6)
		lCity = Label(fMAInput, text="City")
		lCity.grid(column=0, row=7)
		eCity =Entry(fMAInput, width=30)
		eCity.grid(column=1, row=7)
		lState = Label(fMAInput, text="State")
		lState.grid(column=0, row=8)
		eState =Entry(fMAInput, width=30)
		eState.grid(column=1, row=8)
		lZipcode = Label(fMAInput, text="ZIP Code")
		lZipcode.grid(column=0, row=9)
		eZipcode =Entry(fMAInput, width=30)
		eZipcode.grid(column=1, row=9)
		lEmail = Label(fMAInput, text="Email")
		lEmail.grid(column=0, row=10)
		eEmail =Entry(fMAInput, width=30)
		eEmail.grid(column=1, row=10)

		## ordering is important! 
		new_data=[]
		new_data.append(eSsn)
		new_data.append(eFirstName)
		new_data.append(eLastName)
		new_data.append(eEmail)
		new_data.append(eAddr)
		new_data.append(eCity)
		new_data.append(eState)
		new_data.append(eZipcode)
		new_data.append(ePhone)
		new_data.append(eBirthdate)

		data=[]
		data.append(eSsn)
		data.append(eSymptom)
		bSubmit = Button(fMAInput, text="Submit", command=lambda: self.doMakeNewUser([x.get() for x in new_data], [x.get() for x in data]))
		bSubmit.grid(columnspan=2, column=0, row=11)
		return

	def doMakeNewUser(self, userdata, data):
		conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='', db='FinalProject')
		cur = conn.cursor()
		print(data)
		print(userdata)
		now = datetime.datetime.now()
		userdata.insert(3, str(now.year-int(userdata[9].split('-')[0])))
		print("INSERT INTO User VALUES ('"+"','".join(userdata)+"', NULL);")
		cur.execute("INSERT INTO User VALUES ('"+"','".join(userdata)+"', NULL);")
		cur.execute("INSERT INTO Patient VALUES ('%s');"%userdata[0])
		conn.commit()
		self.doMakeAppointment(data)

		conn.close()
		return

	def msgErr(self, errcode):
		errdic = {1: "Not Found!", 2: "Already Existed!", 3:"Input Error!"}
		tkMessageBox.showinfo("Error", errdic[errcode])
		return


	def searchAppointment(self):
		self.clearInfoFrame()
		fSAInput = Frame(self.infoFrame, width=890, height=50)
		fSAInput.pack(fill=BOTH, side=TOP)
		fSAResult = Frame(self.infoFrame, width=890, height=640)
		fSAResult.pack(fill=NONE, side=TOP)

		lAid = Label(fSAInput, text="Appointment SSN").pack(fill=BOTH, side=LEFT)
		eAid = Entry(fSAInput)
		eAid.pack(fill=BOTH, side=LEFT)
		bSearch = Button(fSAInput, text="Search", command=lambda: self.doSearchAppointment(fSAResult, eAid.get())).pack(fill=BOTH, side=LEFT)

		return

	def doSearchAppointment(self, fSAResult, aid):
		conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='', db='FinalProject')
		cur = conn.cursor()
		print(aid)
		lasrow=0
		if not cur.execute("SELECT * FROM Appointment WHERE appointment_sn="+"'"+aid+"'"):
			self.msgErr(1)
		else:
			data=['Appointment Number', 'Doctor SSN', 'Patient SSN', 'Symptom', 'Date', 'Notes']
			for row in cur:
				c=0
				for col in row:
					print(col)
					print(data[c])
					Label(fSAResult, text=data[c], width=20, anchor=W).grid(row=c, column=0)
					Label(fSAResult, text=str(col), width=30, anchor=W).grid(row=c, column=1)
					c=c+1
				lastrow=c-1

		cur.close()

		self.doSearchMedicineByAppointment(fSAResult, aid, lastrow)
		return

	def doSearchMedicineByAppointment(self, fSAResult, aid, lastrow):
		conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='', db='FinalProject')
		cur = conn.cursor()
		print(aid)
		if not cur.execute("SELECT * FROM Appointment_medicine WHERE appointment_sn="+"'"+aid+"'"):
			self.msgErr(1)
		else:
			data=['Medicine Name', 'Shape', 'Producer', 'Functionality', 'Unit Per Time', 'Total Unit']
			for row in cur:
				c=0
				for col in row:
					print(col)
					print(data[c])
					Label(fSAResult, text=data[c], width=20, anchor=W).grid(row=lastrow+c, column=0)
					Label(fSAResult, text=str(col), width=30, anchor=W).grid(row=lastrow+c, column=1)
					c=c+1
		cur.close()
		return

	def searchPatient(self):
		self.clearInfoFrame()
		fSPInput = Frame(self.infoFrame, width=890, height=50)
		fSPInput.pack(fill=BOTH)
		fSPResult = Frame(self.infoFrame, width=890, height=640)
		fSPResult.pack(fill=BOTH)

		lPatientSSN = Label(fSPInput, text="Patient SSN").pack(fill=BOTH, side=LEFT)
		ePatientSSN = Entry(fSPInput)
		ePatientSSN.pack(fill=BOTH, side=LEFT)
		bSearch = Button(fSPInput, text="Search", command=lambda: self.doSearchPatient(fSPResult, ePatientSSN.get())).pack(fill=BOTH, side=LEFT)
		
		return

	def doSearchPatient(self, fSPResult, data):
		conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='', db='FinalProject')
		cur = conn.cursor()
		print(data)
		if not cur.execute("SELECT * FROM Patient WHERE patient_ssn="+"'"+data+"'") or not cur.execute("SELECT * FROM USER WHERE ssn="+"'"+data+"'"):
			self.msgErr(1)
		else:

			data=['SSN', 'First Name', 'Last Name', 'Age', 'Email', 'Address', 'City', 'State', 'ZIP Code', 'Phone', 'Birthday', 'Addition Info']
			for row in cur:
				c=0
				for col in row:
					print(col)
					print(data[c])
					Label(fSPResult, text=data[c], width=15, anchor=W).grid(row=c, column=0)
					Label(fSPResult, text=str(col), width=30, anchor=W).grid(row=c, column=1)
					c=c+1
		cur.close()
		return

	def searchDoctor(self):
		self.clearInfoFrame()
		fSDInput = Frame(self.infoFrame, width=890, height=50)
		fSDInput.pack(fill=BOTH)
		fSDResult = Frame(self.infoFrame, width=890, height=640)
		fSDResult.pack(fill=BOTH)

		lDoctorSSN = Label(fSDInput, text="Doctor SSN").pack(fill=BOTH, side=LEFT)
		eDoctorSSN = Entry(fSDInput)
		eDoctorSSN.pack(fill=BOTH, side=LEFT)
		bSearch = Button(fSDInput, text="Search", command=lambda: self.doSearchDoctor(fSDResult, eDoctorSSN.get())).pack(fill=BOTH, side=LEFT)
		
		return

	def doSearchDoctor(self, fSDResult, data):
		conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='', db='FinalProject')
		cur = conn.cursor()
		print(data)
		if not cur.execute("SELECT * FROM Doctor WHERE doctor_ssn="+"'"+data+"'") or not cur.execute("SELECT * FROM USER WHERE ssn="+"'"+data+"'"):
			self.msgErr(1)
		else:

			data=['SSN', 'First Name', 'Last Name', 'Age', 'Email', 'Address', 'City', 'State', 'ZIP Code', 'Phone', 'Birthday', 'Addition Info']
			for row in cur:
				c=0
				for col in row:
					print(col)
					print(data[c])
					Label(fSDResult, text=data[c], width=15, anchor=W).grid(row=c, column=0)
					Label(fSDResult, text=str(col), width=30, anchor=W).grid(row=c, column=1)
					c=c+1
		cur.close()
		return

	def searchMedicine(self):
		self.clearInfoFrame()
		fSMInput = Frame(self.infoFrame, width=890, height=50)
		fSMInput.pack(fill=BOTH, side=TOP)
		fSMResult = Frame(self.infoFrame, width=890, height=640)
		fSMResult.pack(fill=NONE, side=TOP)

		lName = Label(fSMInput, text="Medicine Name").pack(fill=BOTH, side=LEFT)
		eName = Entry(fSMInput)
		eName.pack(fill=BOTH, side=LEFT)
		bSearch = Button(fSMInput, text="Search", command=lambda: self.doSearchMedicine(fSMResult, eName.get())).pack(fill=BOTH, side=LEFT)

		return

	def doSearchMedicine(self, fSAResult, name):
		conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='', db='FinalProject')
		cur = conn.cursor()
		print(name)
		if not name:
			command = "SELECT * FROM Medicine"
		else:
			command = "SELECT * FROM Medicine WHERE medicine_name='%s'"%name
		
		print(command)
		if not cur.execute(command):
			self.msgErr(1)
		else:
			data=[('Name', 'Shape', 'Producer', 'Functionality', 'Quanlity Having', 'Quanlity Using')]
			colWid=[20, 10, 10, 20, 20, 20]
			for row in cur:
				data.append(row)
			r=0
			for row in data:
				print(row)
				c=0
				for col in row:
					Label(fSAResult, text=str(col), width=colWid[c], anchor=W).grid(row=r, column=c)
					c=c+1
				r=r+1
		cur.close()
		return

	def searchPayment(self):
		self.clearInfoFrame()
		fSPInput = Frame(self.infoFrame, width=890, height=50)
		fSPInput.pack(fill=BOTH)
		fSPResult = Frame(self.infoFrame, width=890, height=640)
		fSPResult.pack(fill=BOTH)

		lAsn = Label(fSPInput, text="Appointment SN").pack(fill=BOTH, side=LEFT)
		eAsn = Entry(fSPInput)
		eAsn.pack(fill=BOTH, side=LEFT)
		bSearch = Button(fSPInput, text="Search", command=lambda: self.doSearchPatient(fSPResult, eAsn.get())).pack(fill=BOTH, side=LEFT)
		
		return

	def doSearchPatient(self, fSPResult, data):
		conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='', db='FinalProject')
		cur = conn.cursor()
		print(data)
		if not cur.execute("SELECT * FROM Appointment WHERE appointment_sn="+"'"+data+"'") or not cur.execute("SELECT * FROM Payment WHERE appointment_sn="+"'"+data+"'"):
			self.msgErr(1)
		else:

			data=['Appointment SN', 'Method', 'Amount', 'Date']
			for row in cur:
				c=0
				for col in row:
					print(col)
					print(data[c])
					Label(fSPResult, text=data[c], width=15, anchor=W).grid(row=c, column=0)
					Label(fSPResult, text=str(col), width=30, anchor=W).grid(row=c, column=1)
					c=c+1
		cur.close()
		return


	def __init__(self):
		root = Tk()

		bottonFrame = Frame(root)
		bottonFrame.pack(fill=BOTH, side=LEFT)

		self.infoFrame = Frame(root, width=900, height=700, bd=5)
		self.infoFrame.pack(fill=BOTH, side=LEFT)

		bMakeAppointment = Button(bottonFrame, text="Make an appointment", width=20, command=self.makeAppointment)
		bMakeAppointment.grid(row=0, column=0, padx=5, pady=5)

		bSearchAppointment = Button(bottonFrame, text="Search an appointment", width=20, command=self.searchAppointment)
		bSearchAppointment.grid(row=1, column=0, padx=5, pady=5)

		bFindDoc = Button(bottonFrame, text="Search a doctor", width=20, command=self.searchDoctor)
		bFindDoc.grid(row=2, column=0, padx=5, pady=5)

		bFindPatient = Button(bottonFrame, text="Search a patient", width=20, command=self.searchPatient)
		bFindPatient.grid(row=3, column=0, padx=5, pady=5)

		bFindMedicine = Button(bottonFrame, text="Search a medicine", width=20, command=self.searchMedicine)
		bFindMedicine.grid(row=4, column=0, padx=5, pady=5)

		bFindPayment = Button(bottonFrame, text="Search a payment", width=20, command=self.searchPayment)
		bFindPayment.grid(row=5, column=0, padx=5, pady=5)

		root.mainloop()

if __name__ == '__main__':
	Appointment()