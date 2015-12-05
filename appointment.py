from Tkinter import *
import tkMessageBox
import pymysql


conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='', db='FinalProject')
cur = conn.cursor()

def submit():
	tkMessageBox.showinfo("Say Hello", "Hello World")
	return

def makeAppointment():
	ma = Tk()
	maFrame = Frame(ma)
	maFrame.pack()
	# lLastName
	# lFirstName
	# lAddr
	# lCity
	# lState
	# lZipcode
	vSsn = StringVar()
	lSsn = Label(maFrame, text="SSN")
	lSsn.grid(column=0, row=0)
	eSsn = Entry(maFrame, textvariable=vSsn)
	eSsn.grid(column=1, row=0)

	vBirthdate = StringVar()
	lBirthdate = Label(maFrame, text="Birthdate")
	lBirthdate.grid(column=0, row=1)
	eBirthdate = Entry(maFrame, textvariable=vBirthdate)
	eBirthdate.grid(column=1, row=1)

	vPhone = StringVar()
	lPhone = Label(maFrame, text="Phone Number")
	lPhone.grid(column=0, row=2)
	ePhone = Entry(maFrame, textvariable=vPhone)
	ePhone.grid(column=1, row=2)

	vSymptom = StringVar()
	lSymptom = Label(maFrame, text="Symtoms")
	lSymptom.grid(column=0, row=3)
	eSymptom = Entry(maFrame, textvariable=vSymptom)
	eSymptom.grid(column=1, row=3)
	# lFirstName
	# lAddr
	# lCity
	# lState
	# lZipcode


	bSubmit = Button(maFrame, text="Submit", command=submit)
	bSubmit.grid(columnspan=2, column=0, row=4)
	ma.mainloop()
	return

def searchAppointment():
	sa = Tk()
	saFrame = Frame(sa)
	saFrame.pack()

	lAid = Label(saFrame, text="Appointment Number")
	lAid.grid(column=0, row=0)
	eAid = Entry(saFrame)
	eAid.grid(column=1, row=0)

	bSearch = Button(saFrame, text="Search", command=lambda:doSearchAppointment(eAid.get()))
	bSearch.grid(columnspan=2, column=0, row=1)
	return

def doSearchAppointment(aid):
	print(aid)
	if not cur.execute("SELECT * FROM Appointment WHERE appointment_sn="+"'"+aid+"'"):
		print("Not found!")
	else:
		data=[('Appointment Number', 'Doctor SSN', 'Patient SSN', 'Symptom', 'Date', 'Notes')]

		for row in cur:
			data.append(row)
		r=0
		for row in data:
			print(row)
			c=0
			for col in row:
				Label(infoFrame, text=col, width=20, anchor=W).grid(row=r, column=c)
				c=c+1
			r=r+1
	return


def showInfo():
	fInfo = Frame(infoFrame, width=500, height=500, bg="yellow")
	fInfo.grid(column=0, row=0)
	lInfo = Label(fInfo, text="let's rock the world!")
	lInfo.grid(column=0, row=0)
	return


root = Tk()

bottonFrame = Frame(root)
bottonFrame.pack(fill=BOTH, side=LEFT)

infoFrame = Frame(root, width=900, height=900, bd=5)
infoFrame.pack(fill=BOTH, side=LEFT)

bMakeAppointment = Button(bottonFrame, text="Make an appointment", width=20, command=makeAppointment)
bMakeAppointment.grid(row=0, column=0, padx=5, pady=5)

bSearchAppointment = Button(bottonFrame, text="Search an appointment", width=20, command=searchAppointment)
bSearchAppointment.grid(row=1, column=0, padx=5, pady=5)

bFindDoc = Button(bottonFrame, text="Search a doctor", width=20, command=showInfo)
bFindDoc.grid(row=2, column=0, padx=5, pady=5)

bFindPatient = Button(bottonFrame, text="Search a patient", width=20)
bFindPatient.grid(row=3, column=0, padx=5, pady=5)

bFindMedicine = Button(bottonFrame, text="Search a medicine", width=20)
bFindMedicine.grid(row=4, column=0, padx=5, pady=5)

bFindPayment = Button(bottonFrame, text="Search a payment", width=20)
bFindPayment.grid(row=5, column=0, padx=5, pady=5)


root.mainloop()