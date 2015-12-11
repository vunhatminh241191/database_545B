DROP DATABASE FinalProject;
Create Database FinalProject;
USE FinalProject;

CREATE TABLE User (
    ssn                 Integer         NOT NULL,
    first_name          Char(32)        NOT NULL,
    last_name           Char(32)        NOT NULL,
    age                 Integer         NOT NULL,
    email               Char(64)        NOT NULL,
    address             Char(64)        NOT NULL,
    city                Char(64)        NOT NULL,
    state               Char(8)         NOT NULL,
    zip_code            Integer         NOT NULL,
    phone               Char(16)        NOT NULL,
    date_of_birth       Char(16)          NOT NULL,
    additional_info     Char(64)        NULL,
    PRIMARY KEY (ssn)
    ); 

CREATE TABLE Doctor (
    doctor_ssn                  Integer         NOT NULL,
    doctor_licensing_number     Char(8)         NOT NULL,   
    PRIMARY KEY (doctor_ssn),
    FOREIGN KEY (doctor_ssn)    REFERENCES User(ssn)
    );

CREATE TABLE Doctor_specilist (
    doctor_ssn                  Integer         NOT NULL,
    subject                     Char(64)        NOT NULL,
    PRIMARY KEY (doctor_ssn),
    FOREIGN KEY (doctor_ssn) REFERENCES Doctor(doctor_ssn)
    );

CREATE TABLE Patient (
    patient_ssn                 Integer        NOT NULL,
    FOREIGN KEY (patient_ssn)   REFERENCES User(ssn),
    PRIMARY KEY (patient_ssn)
    );

CREATE TABLE Appointment (
    appointment_sn      Char(8)         NOT NULL,
    doctor_ssn          Integer         NULL,
    patient_ssn         Integer         NOT NULL,
    symptoms            Char(64)        NOT NULL,
    appointment_date    Char(10)        NOT NULL,
    notes               Char(128)       NULL,
    PRIMARY KEY (appointment_sn),
    FOREIGN KEY (patient_ssn)   REFERENCES Patient(patient_ssn),
    FOREIGN KEY (doctor_ssn)    REFERENCES Doctor(doctor_ssn)
    );

CREATE TABLE Medicine (
    medicine_name   Char(64)        NOT NULL,
    shape           Char(16)        NOT NULL,
    producer        Char(16)        NOT NULL,           
    functionality   Char(64)        NULL,
    quanlity_having Integer         NULL,
    quanlity_using  Integer         NULL,
    PRIMARY KEY (medicine_name, shape, producer)
    );
    
CREATE TABLE Appointment_medicine (
    appointment_sn  Char(8)         NOT NULL,
    medicine_name   Char(64)        NOT NULL,
    shape           Char(16)        NOT NULL,
    producer        Char(16)        NOT NULL, 
    unit_per_time   Integer         NOT NULL,
    total_unit      Integer         NOT NULL,
    PRIMARY KEY (appointment_sn, medicine_name, shape, producer),
    FOREIGN KEY (appointment_sn)    REFERENCES Appointment(appointment_sn),
    FOREIGN KEY (medicine_name, shape, producer) REFERENCES Medicine(medicine_name, shape, producer)
    );


CREATE TABLE Payment (
    appointment_sn  Char(8)         NOT NULL,
    payment_method  Char(16)        NOT NULL,
    amount_of_money Integer         NOT NULL,
    date            Char(10)        NOT NULL,
    FOREIGN KEY (appointment_sn)    REFERENCES Appointment(appointment_sn),
    PRIMARY KEY (appointment_sn, date)
    );


INSERT INTO User VALUES ('100000001', 'Shirley B.', 'Lindquist', '22', 'ShirleyBLindquist@dayrep.com', '2596 Settlers Lane', 'New York', 'NY', '10016', '9177622342', '1993-02-16', NULL);
INSERT INTO User VALUES ('100000002', 'Richard A.', 'Chase', '60', 'RichardAChase@armyspy.com', '3939 Larry Street', 'Milwaukee', 'WI', '53226', '4148903514', '1955-04-06', NULL); 
INSERT INTO User VALUES ('100000003', 'Ben E.', 'Wetzel', '43', 'BenEWetzel@dayrep.com', '124 Edington Drive', 'Norcross', 'GA', '30071', '6788236568', '1972-5-24', NULL);
INSERT INTO User VALUES ('100000004', 'Dana D.', 'Figueroa', '29', 'DanaDFigueroa@jourrapide.com', '2928 Turnpike Drive', 'Huntsville', 'AL', '35802', '2563822832', '1986-5-26', NULL);
INSERT INTO User VALUES ('100000005', 'Paula M.', 'Mills', '63', 'PaulaMMills@armyspy.com', '4928 Crowfield Road', 'Phoenix', 'AZ', '85012', '6028068357', '1952-8-2', NULL);
INSERT INTO User VALUES ('100000006', 'Angie L.', 'Shimer', '52', 'AngieLShimer@jourrapide.com', '39 Mandan Road', 'Steelville', 'MO', '65565', '5737755158', '1963-5-15', NULL);
INSERT INTO User VALUES ('100000007', 'Teresa B.', 'Obrien', '68', 'TeresaBObrien@jourrapide.com', '2322 Richards Avenue', 'Stockton', 'CA', '95204', '2098677769', '1947-8-12', NULL);
INSERT INTO User VALUES ('100000008', 'John H.', 'Burch', '20', 'JohnHBurch@rhyta.com', '2069 Vineyard Drive', 'Springfield', 'OH', '44124', '4404462804', '1995-5-2', NULL);
INSERT INTO User VALUES ('100000009', 'Vanessa T.', 'Quintero', '66', 'VanessaTQuintero@rhyta.com', '331 Stewart Street', 'Indianapolis', 'IN', '46214', '3176641680', '1949-5-29', NULL);
INSERT INTO User VALUES ('100000010', 'Jack J.', 'Beadle', '67', 'JackJBeadle@jourrapide.com', '552 Hawks Nest Lane', 'Stlouis', 'MO', '63101', '3147064673', '1948-8-11', NULL);
INSERT INTO User VALUES ('100000011', 'Mercedes K.', 'Miller', '53', 'MercedesKMiller@rhyta.com', '3573 Norma Avenue', 'Dayton', 'OH', '45406', '9372146090', '1962-8-11', NULL);
INSERT INTO User VALUES ('100000012', 'Patricia C.', 'Jasper', '21', 'PatriciaCJasper@jourrapide.com', '3208 Ralph Drive', 'Warrensville Heights', 'OH', '44128', '4403014540', '1994-5-22', NULL);
INSERT INTO User VALUES ('100000013', 'Candis J.', 'Larochelle', '37', 'CandisJLarochelle@jourrapide.com', '2140 Kemper Lane', 'Salt Lake City', 'UT', '84116', '8018654654', '1978-10-14', NULL);
INSERT INTO User VALUES ('100000014', 'Gladys K.', 'Allen', '34', 'GladysKAllen@jourrapide.com', '4830 Pointe Lane', 'Pompano Beach', 'FL', '33060', '9549687070', '1981-2-12', NULL);
INSERT INTO User VALUES ('100000015', 'Kathy J.', 'Pena', '65', 'KathyJPena@jourrapide.com', '4693 Washington Avenue', 'Jackson', 'MS', '39211', '6019934205', '1950-10-29', NULL);
INSERT INTO User VALUES ('100000016', 'Marge L.', 'Cordova', '53', 'MargeLCordova@teleworm.us', '4482 Ripple Street', 'Saginaw', 'MI', '48607', '9897554339', '1962-6-17', NULL);
INSERT INTO User VALUES ('100000017', 'Margene C.', 'Allen', '21', 'MargeneCAllen@armyspy.com', '376 Dennison Street', 'Sonora', 'CA', '95370', '2095339648', '1994-1-10', NULL);
INSERT INTO User VALUES ('100000018', 'Ricardo G.', 'Williams', '35', 'RicardoGWilliams@jourrapide.com', '2864 Lunetta Street', 'Bluegrove', 'TX', '76352', '9408955717', '1979-12-3', NULL);
INSERT INTO User VALUES ('100000019', 'Sara R.', 'Nash', '37', 'SaraRNash@rhyta.com', '123 Dola Mine Road', 'Raleigh', 'NC', '27607', '9193453110', '1977-11-3', NULL);
INSERT INTO User VALUES ('100000020', 'Kathy R.', 'Allen', '22', 'KathyRAllen@rhyta.com', '456 Dennison Street', 'Sonora', 'CA', '95370', '2095339558', '1992-11-3', NULL);


INSERT INTO Medicine VALUES ('Fever A', 'Oval', 'A', 'Fever level 1', 2000, 80);
INSERT INTO Medicine VALUES ('Headache Assistant', 'Circle', 'G', 'Headache level 2', 1000, 350);
INSERT INTO Medicine VALUES ('Balling B', 'capsule', 'A', 'Balling Level 1', 500, 200);
INSERT INTO Medicine VALUES ('Fever B', 'capsule', 'A', 'Fever level 3', 5000, 3000);
INSERT INTO Medicine VALUES ('Stomachache Hurt', 'Rectangle', 'D', 'Stomachache level 4', 1000, 10);
INSERT INTO Medicine VALUES ('Headache Assistant', 'Oval', 'Z', 'Headache level 1', 3000, 1580);
INSERT INTO Medicine VALUES ('Stomachache health', 'Circle', 'Z', 'Stomachache level 1', 200, 0);
INSERT INTO Medicine VALUES ('Dizziness Easy Gone', 'Rectangle', 'B', 'Dizziness level 1', 400, 50);
INSERT INTO Medicine VALUES ('Dizziness Get Away', 'Oval', 'K', 'Dizziness level 3', 200, 10);
INSERT INTO Medicine VALUES ('Headache Hurt', 'capsule', 'J', 'Headache level 3', 100, 20);

INSERT INTO Patient VALUES ('100000011');
INSERT INTO Patient VALUES ('100000012');
INSERT INTO Patient VALUES ('100000013');
INSERT INTO Patient VALUES ('100000014');
INSERT INTO Patient VALUES ('100000015');
INSERT INTO Patient VALUES ('100000016');
INSERT INTO Patient VALUES ('100000017');
INSERT INTO Patient VALUES ('100000018');
INSERT INTO Patient VALUES ('100000019');
INSERT INTO Patient VALUES ('100000020');

INSERT INTO Doctor VALUES ('100000001','A25678');
INSERT INTO Doctor VALUES ('100000002','B27804');
INSERT INTO Doctor VALUES ('100000003','H18083');
INSERT INTO Doctor VALUES ('100000004','K00023');
INSERT INTO Doctor VALUES ('100000005','N89014');
INSERT INTO Doctor VALUES ('100000006','A33311');
INSERT INTO Doctor VALUES ('100000007','V56732');
INSERT INTO Doctor VALUES ('100000008','W24567');
INSERT INTO Doctor VALUES ('100000009','Q12389');
INSERT INTO Doctor VALUES ('100000010','T45612');

INSERT INTO Appointment VALUES ('1111', '100000008', '100000011', 'Fever', '2015-02-08', 'Not Important');
INSERT INTO Appointment VALUES ('1112', '100000005', '100000012', 'Headache', '2015-03-07', 'Headache level 4, should look at this');
INSERT INTO Appointment VALUES ('1113', '100000007', '100000013', 'Headache', '2015-04-08', 'Headache level 4, already using 10 pills level 2');
INSERT INTO Appointment VALUES ('1114', '100000002', '100000014', 'Stomachache', '2015-05-18', 'Not Important');
INSERT INTO Appointment VALUES ('1115', '100000002', '100000015', 'Stomachache', '2015-06-20', 'After using these pills, should be fine');
INSERT INTO Appointment VALUES ('1116', '100000005', '100000016', 'Dizziness', '2015-07-03', 'Symptoms just begins, need to look at');
INSERT INTO Appointment VALUES ('1117', '100000007', '100000017', 'Dizziness', '2015-07-20', 'Should go to hospital frequently to check');
INSERT INTO Appointment VALUES ('1118', '100000005', '100000018', 'Headache', '2015-08-12', 'Not Important');
INSERT INTO Appointment VALUES ('1119', '100000004', '100000019', 'Balling', '2015-09-22', 'Balling level 1, needing 2 weeks to recover');
INSERT INTO Appointment VALUES ('1120', '100000008', '100000020', 'Fever', '2015-10-15', 'Should take a rest');

INSERT INTO Doctor_specilist VALUES ('100000001', 'Headache');
INSERT INTO Doctor_specilist VALUES ('100000002', 'Stomachache');
INSERT INTO Doctor_specilist VALUES ('100000003', 'Stomachache');
INSERT INTO Doctor_specilist VALUES ('100000004', 'Balling');
INSERT INTO Doctor_specilist VALUES ('100000005', 'Headache');
INSERT INTO Doctor_specilist VALUES ('100000006', 'Eye');
INSERT INTO Doctor_specilist VALUES ('100000007', 'Headache');
INSERT INTO Doctor_specilist VALUES ('100000008', 'Allergy');
INSERT INTO Doctor_specilist VALUES ('100000009', 'Heart');
INSERT INTO Doctor_specilist VALUES ('100000010', 'Liver');

INSERT INTO Appointment_medicine VALUES('1111', 'Fever A', 'Oval', 'A', 2, 10);
INSERT INTO Appointment_medicine VALUES('1112', 'Headache Hurt', 'capsule', 'J', 1, 10);
INSERT INTO Appointment_medicine VALUES('1113', 'Headache Hurt', 'capsule', 'J', 2, 5);
INSERT INTO Appointment_medicine VALUES('1114', 'Stomachache health', 'Circle', 'Z', 0.5, 8);
INSERT INTO Appointment_medicine VALUES('1115', 'Stomachache Hurt', 'Rectangle', 'D', 1.5, 2);
INSERT INTO Appointment_medicine VALUES('1116', 'Dizziness Easy Gone', 'Rectangle', 'B', 1, 3);
INSERT INTO Appointment_medicine VALUES('1117', 'Dizziness Get Away', 'Oval', 'K', 1, 4);
INSERT INTO Appointment_medicine VALUES('1118', 'Headache Assistant', 'Oval', 'Z', 1.5, 9);
INSERT INTO Appointment_medicine VALUES('1119', 'Balling B', 'capsule', 'A', 2, 8);
INSERT INTO Appointment_medicine VALUES('1120', 'Fever B', 'capsule', 'A', 2, 1);

INSERT INTO Payment VALUES ('1111', 'CASH', 180, '2015-02-08');
INSERT INTO Payment VALUES ('1112', 'DEBIT', 250, '2015-03-07');
INSERT INTO Payment VALUES ('1113', 'CREDIT', 100, '2015-04-08');
INSERT INTO Payment VALUES ('1114', 'CASH', 80, '2015-05-18');
INSERT INTO Payment VALUES ('1115', 'CASH', 60, '2015-06-20');
INSERT INTO Payment VALUES ('1116', 'CREDIT', 400, '2015-07-03');
INSERT INTO Payment VALUES ('1117', 'CREDIT', 250, '2015-07-20');
INSERT INTO Payment VALUES ('1118', 'DEBIT', 50, '2015-08-12');
INSERT INTO Payment VALUES ('1119', 'CREDIT', 90, '2015-09-22');
INSERT INTO Payment VALUES ('1120', 'CASH', 70, '2015-10-15');