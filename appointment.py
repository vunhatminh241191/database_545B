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

	vAid = StringVar()
	lAid = Label(saFrame, text="Appointment ID")
	lAid.grid(column=0, row=0)
	eAid = Entry(saFrame, textvariable=vAid)
	eAid.grid(column=1, row=0)

	bSearch = Button(saFrame, text="Search", command=doSearchAppointment)
	bSearch.grid(columnspan=2, column=0, row=1)
	return

def doSearchAppointment():
	# print(aid)
	cur.execute("SELECT * FROM Appointment WHERE appointment_sn='1111'")
	# if not cur.fetchone():
	# 	print("Not found!")
	for row in cur:
		print(row)
	return


def showInfo():
	fInfo = Frame(infoFrame, width=500, height=500, bg="yellow")
	fInfo.grid(column=0, row=0)
	lInfo = Label(fInfo, text="let's rock the world!")
	lInfo.grid(column=0, row=0)
	return


root = Tk()

bottonFrame = Frame(root)
bottonFrame.grid(row=0,column=0)

infoFrame = Frame(root, width=500, height=500,bg="white")
infoFrame.grid(row=0,column=1)

bMakeAppointment = Button(bottonFrame, text="Make an appointment", width=20, command=makeAppointment)
bMakeAppointment.grid(row=0, column=0)

bSearchAppointment = Button(bottonFrame, text="Search an appointment", width=20, command=searchAppointment)
bSearchAppointment.grid(row=1, column=0)

bFindDoc = Button(bottonFrame, text="Search a doctor", width=20, command=showInfo)
bFindDoc.grid(row=2, column=0)

bFindPatient = Button(bottonFrame, text="Search a patient", width=20)
bFindPatient.grid(row=3, column=0)

bFindMedicine = Button(bottonFrame, text="Search a medicine", width=20)
bFindMedicine.grid(row=4, column=0)

bFindPayment = Button(bottonFrame, text="Search a payment", width=20)
bFindPayment.grid(row=5, column=0)


root.mainloop()