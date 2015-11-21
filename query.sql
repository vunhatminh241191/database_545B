Create Database FinalProject;
USE FinalProject;

CREATE TABLE User (
	ssn					Char(16)       	NOT NULL,
	first_ame     		Char(32) 	    NOT NULL,
    second_Name			Char(32)		NOT NULL,
    age					Integer			NOT NULL,
    email				Char(64)		NOT NULL,
    address				Char(64)		NOT NULL,
    city				Char(16)		NOT NULL,
    state				Char(16)		NOT NULL,
    zip_code			Integer			NOT NULL,
    phone				Integer			NOT NULL,
    date_of_birth		Char(10)		NOT NULL,
    additional_info		Char(64)		NULL,
    FOREIGN KEY (addr_id) 	REFERENCES Address(addr_id),
	PRIMARY KEY (ssn)
	);

CREATE TABLE Doctor (
	doctor_ssn					Char(16)       	NOT NULL,
	nurse_licensing_number      Integer 	    NOT NULL,	
	FOREIGN KEY (doctor_ssn) 	REFERENCES User(ssn),
	PRIMARY KEY (doctor_ssn)
	);

CREATE TABLE Patient (
	patient_ssn					Char(16)       	NOT NULL,
	FOREIGN KEY (patient_ssn) 	REFERENCES User(ssn),
	PRIMARY KEY (patient_ssn)
	);

CREATE TABLE Appointment (
	appointment_id		Integer			NOT NULL,
	patient_ssn			Char(16)       	NOT NULL,
	doctor_ssn			Char(16)        NOT NULL,
	symptoms			Char(64)		NOT NULL,
	appointment_date	Char(10)		NOT NULL,
	FOREIGN KEY (patient_ssn) 	REFERENCES Patient(ssn),
	FOREIGN KEY (doctor_ssn) 	REFERENCES Doctor(ssn),
	PRIMARY KEY (appointment_id)
	);

CREATE TABLE Medicine (
	name			Char(16)       	NOT NULL,
	shape			Char(16)        NOT NULL,
	producer		Char(16)		NOT NULL,			
	unit_per_time	Char(10)		NOT NULL,
	quanlity_having	Integer			NULL,
	quanlity_using	Integer			NULL,
	PRIMARY KEY (name, shape, producer)
	);

CREATE TABLE Payment (
	appointment_id	Integer			NOT NULL,
	patient_ssn		Char(16)       	NOT NULL,
	payment_method	Char(16)        NOT NULL,
	amount_of_money	Integer			NOT NULL,
	date 			Char(10)		NOT NULL,
	FOREIGN KEY (patient_ssn) 		REFERENCES Patient(ssn),
	FOREIGN	KEY	(appointment_id)	REFERENCES Appointment(appointment_id),
	PRIMARY KEY (patient_ssn)
	);

CREATE TABLE Note (
	appointment_id		Integer			NOT NULL,
	medicine_name		Char(16)       	NOT NULL,
	appointment			Char(16)        NOT NULL,
	notes_date			char(10)		NOT NULL,
	FOREIGN	KEY	(appointment_id)	REFERENCES Appointment(appointment_id),
	FOREIGN KEY (medicine_name) 	REFERENCES Medicine(name),
	FOREIGN KEY (doctor_ssn) 		REFERENCES Doctor(ssn),
	PRIMARY KEY (appointment_id)
	);


